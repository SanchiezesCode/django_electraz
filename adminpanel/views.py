from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse  # добавьте этот импорт
from django.http import HttpResponse, JsonResponse, QueryDict
from electrazapi.models import Client, ManufacturerProduct, Supplier, asdf
from django.urls import reverse_lazy
from django.db import IntegrityError
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.forms import modelform_factory
import re
from django.contrib import messages
from django.core.serializers.json import DjangoJSONEncoder
from django.core.exceptions import ValidationError

import json
import logging
maindata = {

}
 
def index(request):
    context = {
        'title' : 'Статистика',
    }
    return render(request, "adminpanel/index.html", context = context)

def ShowProduct_list(request):
    context = {
        'title' : 'Список товаров',
    }
    return render(request, "adminpanel/product_list.html", context = context)

def ShowProduct_category(request):
    context = {
        'title': 'Категории товаров',
    }
    return render(request, "adminpanel/product_category.html", context=context)

def ShowProduct_manufacturer(request): 
    context = {
        'title': 'Производители',
    }
    return render(request, "adminpanel/product_manufacturer.html", context=context)

def ShowProduct_add(request): 
    context = {
        'title': 'Добавить товар',
    }
    
    return render(request, "adminpanel/product_add.html", context=context)




def ShowCrm_leads(request):
    context = {
        'title' : 'Заявки',
    }
    return render(request, "adminpanel/crm_leads.html", context = context)

def ShowCrm_add(request):
    context = {
        'title' : 'Новый клиент',
    }
    return render(request, "adminpanel/crm_add.html", context = context)

def ShowMainCalcPage(request):

    return render(request, "adminpanel/maincalc.html")

def upload_file(request):
    if request.method == 'POST':
        myfile = request.FILES['myfile']

        print('Hello World!')
        # Далее можно обработать загруженный файл, например, сохранить его на сервере или выполнить какие-то другие действия
        return HttpResponse('Файл успешно загружен.')
    return render(request, 'upload.html')

def get_column_value(obj, column):
    return obj.get(column, '')

def parse_multipart_form_data(body):
    # Разделяем тело запроса по уникальному разделителю
    boundary = body.split(b'\r\n')[0]
    # Разделяем данные на части
    parts = re.split(boundary, body)
    # Удаляем пустые строки и последний элемент, который является пустым после разделителя
    parts = [part for part in parts if part and part != b'--\r\n']
    
    # Создаем словарь для хранения данных
    data = {}
    
    for part in parts:
        # Разделяем части на заголовки и содержимое
        headers, content = part.split(b'\r\n\r\n', 1)
        content = content.rstrip(b'\r\n')  # Удаляем перенос строки в конце содержимого
        
        # Ищем имя поля в заголовках
        name_match = re.search(b'name="([^"]+)"', headers)
        if name_match:
            name = name_match.group(1).decode('utf-8')
            # Добавляем содержимое в словарь данных
            data[name] = content.decode('utf-8')
    
    # Преобразуем словарь в QueryDict
    query_dict = QueryDict('', mutable=True)
    for key, value in data.items():
        query_dict.setlist(key, [value])
    
    return query_dict

def model_list_view(request, model, columns, form_columns=None, edit_columns=None, is_deletable=True, show_id=False):
    model_name = model._meta.model_name
    model_name_verbose = model._meta.verbose_name
    model_name_verbose_plural = model._meta.verbose_name_plural
    model_name_verbose_name_table_add = model.get_verbose_name_table_add()
    model_name_verbose_name_table = model.get_verbose_name_table()

    objects = model.objects.all()

    if show_id:
        columns_verbose = {id: '#'}
    else:
        columns_verbose = {}
    
    for field_name in columns:
        field = model._meta.get_field(field_name)
        columns_verbose[field_name] = field.verbose_name

    if edit_columns:
        EditModelForm = modelform_factory(model, fields=edit_columns)
        edit_form = EditModelForm()
        class UniqueNameEditModelForm(EditModelForm):
            def clean_name(self):
                name = self.cleaned_data.get('name')
                if model.objects.filter(name=name).exists():
                    raise ValidationError(f'{model._meta.verbose_name.capitalize()} с именем "{name}" уже существует.')
                return name
            
    # Добавляем столбец 'id' в начало списка, если его там нет
    if 'id' not in columns:
        columns = ['id'] + columns

    objects_with_names = []
    for obj in objects:
        values = []
        for column in columns:
            field = model._meta.get_field(column)
            if hasattr(obj, column):
                if field.is_relation and field.many_to_one:
                    related_obj = getattr(obj, column)
                    related_name = related_obj.__str__()
                    values.append(related_name)
                else:
                    value = getattr(obj, column)
                    values.append(value)
        objects_with_names.append(values)

    if form_columns:
        ModelForm = modelform_factory(model, fields=form_columns)
        class UniqueNameModelForm(ModelForm):
            def clean_name(self):
                name = self.cleaned_data.get('name')
                if model.objects.filter(name=name).exists():
                    raise ValidationError(f'{model._meta.verbose_name.capitalize()} с именем "{name}" уже существует.')
                return name
        if request.method == 'POST':
            form = UniqueNameModelForm(request.POST)
            try:
                if form.is_valid():
                    form.save()
                    # Отправляем JSON-ответ в случае успеха
                    print('11')
                    return JsonResponse({'status': 'success', 'message': 'Запись успешно добавлена.'})
                else:
                    # Отправляем JSON-ответ с ошибками
                    print('22')
                    return JsonResponse({'status': 'error', 'message': form.errors.as_json()}, status=400)
            except ValidationError as e:
                print('33')
                # Отправляем JSON-ответ с ошибкой валидации
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    else:
        form = None

    if request.method == 'DELETE':
        # Получаем данные из тела запроса
        data = json.loads(request.body)
        pk = data.get('pk')

        if pk is not None:
            try:
                # Получаем объект для удаления или возвращаем ошибку 404, если объект не найден
                obj = get_object_or_404(model, pk=pk)
                delete_value = getattr(obj, columns[1])
                print(delete_value)
                # Удаляем объект
                obj.delete()
                # Возвращаем успешный ответ
                return JsonResponse({'message': f'Объект "{delete_value}" был успешно удален.'})
            except model.DoesNotExist:
                return JsonResponse({'error': 'Объект не найден.'}, status=404)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({'error': 'Первичный ключ не предоставлен.'}, status=400)

            
    if edit_columns:
        EditModelForm = modelform_factory(model, fields=edit_columns)
        class UniqueNameEditModelForm(EditModelForm):
            def clean_name(self):
                name = self.cleaned_data.get('name')
                if model.objects.filter(name=name).exclude(pk=self.instance.pk).exists():
                    raise ValidationError(f'{model._meta.verbose_name.capitalize()} с именем "{name}" уже существует.')
                return name
            
        if request.method == 'PUT':
            # Извлекаем данные из тела запроса
            data = parse_multipart_form_data(request.body)
            pk = data.get('id')
            if pk is not None:
                obj = get_object_or_404(model, pk=pk)
                edit_form = UniqueNameEditModelForm(data, instance=obj)  # Связываем форму с данными из запроса и существующим объектом
                if edit_form.is_valid():
                    try:
                        edit_form.save()
                        return JsonResponse({'status': 'success', 'message': 'Данные обновлены.'}, status=200)
                    except ValidationError as e:
                        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
                else:
                    return JsonResponse({'status': 'error', 'message': edit_form.errors.as_json()}, status=400)
            else:
                return JsonResponse({'status': 'error', 'message': 'Первичный ключ не предоставлен.'}, status=400)
    else:
        edit_form = None
        





        

    
    def get_field_types(model):
        field_types = {}
        for field in model._meta.fields:
            field_name = field.name
            field_type = field.get_internal_type()
            base_classes = [base.__name__ for base in field.__class__.__bases__]
            print(f"Field: {field_name}, Type: {field_type}, Base classes: {base_classes}")
            field_types[field_name] = field_type
        return field_types
    instance = model()
    field_types = {field.name: type(field).__name__ for field in instance._meta.fields}


    # Передаем сообщения в шаблон в формате JSON
    message_data = json.dumps([{
        'level': message.level_tag,
        'text': message.message,
    } for message in messages.get_messages(request)], cls=DjangoJSONEncoder)

    context = {
        'model_name': model_name,
        'model_name_verbose': model_name_verbose,
        'model_name_verbose_plural': model_name_verbose_plural,
        'model_name_verbose_name_table':model_name_verbose_name_table,
        'model_name_verbose_name_table_add':model_name_verbose_name_table_add,
        'columns': columns,
        'columns_verbose': columns_verbose,
        'edit_columns': edit_columns,
        'objects': objects_with_names,
        'form': form,
        'edit_form': edit_form,
        'is_deletable': is_deletable,
        'show_id': show_id,
        'field_types': field_types,
        'message_data_json': message_data  # Добавлено для SweetAlert
    }

    return render(request, 'adminpanel/base_for_models.html', context)




# Пример использования в представлении crm_clients
def crm_clients(request):
    model = Client
    table_columns = ['first_name', 'email', 'phone_number']
    edit_columns = ['first_name', 'email', 'phone_number']
    form_columns = ['first_name', 'email', 'phone_number']
    return model_list_view(request, model, table_columns, form_columns, edit_columns)

def ShowManufacturer_country(request):
    model = ManufacturerProduct
    table_columns = ['name', 'country']
    is_deletable = True
    edit_columns = table_columns
    form_columns = ['name', 'country']
    return model_list_view(request, model, table_columns, form_columns, edit_columns, is_deletable)

def ShowSupplier_list(request):
    model = Supplier
    columns = ['link', 'name']
    show_id = False
    edit_columns = None
    is_deletable = False
    form_columns = None
    return model_list_view(request, model, columns, form_columns, edit_columns, is_deletable, show_id)


    