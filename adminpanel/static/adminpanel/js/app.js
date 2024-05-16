"use strict";
function _typeof(e) {
    return (_typeof =
        "function" == typeof Symbol && "symbol" == typeof Symbol.iterator
            ? function (e) {
                  return typeof e;
              }
            : function (e) {
                  return e && "function" == typeof Symbol && e.constructor === Symbol && e !== Symbol.prototype ? "symbol" : typeof e;
              })(e);
}
function _classCallCheck(e, t) {
    if (!(e instanceof t)) throw new TypeError("Cannot call a class as a function");
}
function _defineProperties(e, t) {
    for (var n = 0; n < t.length; n++) {
        var a = t[n];
        (a.enumerable = a.enumerable || !1), (a.configurable = !0), "value" in a && (a.writable = !0), Object.defineProperty(e, _toPropertyKey(a.key), a);
    }
}
function _createClass(e, t, n) {
    return t && _defineProperties(e.prototype, t), n && _defineProperties(e, n), Object.defineProperty(e, "prototype", { writable: !1 }), e;
}
function _toPropertyKey(e) {
    var t = _toPrimitive(e, "string");
    return "symbol" === _typeof(t) ? t : String(t);
}
function _toPrimitive(e, t) {
    if ("object" !== _typeof(e) || null === e) return e;
    var n = e[Symbol.toPrimitive];
    if (void 0 === n) return ("string" === t ? String : Number)(e);
    var a = n.call(e, t || "default");
    if ("object" !== _typeof(a)) return a;
    throw new TypeError("@@toPrimitive must return a primitive value.");
}
function _toConsumableArray(e) {
    return _arrayWithoutHoles(e) || _iterableToArray(e) || _unsupportedIterableToArray(e) || _nonIterableSpread();
}
function _nonIterableSpread() {
    throw new TypeError("Invalid attempt to spread non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method.");
}
function _unsupportedIterableToArray(e, t) {
    if (e) {
        if ("string" == typeof e) return _arrayLikeToArray(e, t);
        var n = Object.prototype.toString.call(e).slice(8, -1);
        return "Object" === n && e.constructor && (n = e.constructor.name), "Map" === n || "Set" === n ? Array.from(e) : "Arguments" === n || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n) ? _arrayLikeToArray(e, t) : void 0;
    }
}
function _iterableToArray(e) {
    if (("undefined" != typeof Symbol && null != e[Symbol.iterator]) || null != e["@@iterator"]) return Array.from(e);
}
function _arrayWithoutHoles(e) {
    if (Array.isArray(e)) return _arrayLikeToArray(e);
}
function _arrayLikeToArray(e, t) {
    (null == t || t > e.length) && (t = e.length);
    for (var n = 0, a = new Array(t); n < t; n++) a[n] = e[n];
    return a;
}
!(function (r) {
    function e() {
        r(window).on("load", function () {
            r("#status").fadeOut(), r("#preloader").delay(350).fadeOut("slow");
        });
        _toConsumableArray(document.querySelectorAll('[data-bs-toggle="popover"]')).map(function (e) {
            return new bootstrap.Popover(e);
        }),
            _toConsumableArray(document.querySelectorAll('[data-bs-toggle="tooltip"]')).map(function (e) {
                return new bootstrap.Tooltip(e);
            }),
            _toConsumableArray(document.querySelectorAll(".offcanvas")).map(function (e) {
                return new bootstrap.Offcanvas(e);
            });
        var e = document.getElementById("toastPlacement");
        e &&
            document.getElementById("selectToastPlacement").addEventListener("change", function () {
                e.dataset.originalClass || (e.dataset.originalClass = e.className), (e.className = e.dataset.originalClass + " " + this.value);
            });
        [].slice.call(document.querySelectorAll(".toast")).map(function (e) {
            return new bootstrap.Toast(e);
        });
        var a = document.getElementById("liveAlertPlaceholder"),
            t = document.getElementById("liveAlertBtn");
        t &&
            t.addEventListener("click", function () {
                var e, t, n;
                (e = "Nice, you triggered this alert message!"),
                    (t = "success"),
                    ((n = document.createElement("div")).innerHTML = [
                        '<div class="alert alert-'.concat(t, ' alert-dismissible" role="alert">'),
                        "   <div>".concat(e, "</div>"),
                        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>',
                        "</div>",
                    ].join("")),
                    a.append(n);
            }),
            document.getElementById("app-style").href.includes("rtl.min.css") && (document.getElementsByTagName("html")[0].dir = "rtl");
        var n = r(this).attr("data-delay") ? r(this).attr("data-delay") : 100,
            o = r(this).attr("data-time") ? r(this).attr("data-time") : 1200;
        r('[data-plugin="counterup"]').each(function (e, t) {
            r(this).counterUp({ delay: n, time: o });
        }),
            0 < r('[data-plugin="tippy"]').length && tippy('[data-plugin="tippy"]'),
            r("[data-password]").on("click", function () {
                "false" == r(this).attr("data-password")
                    ? (r(this).siblings("input").attr("type", "text"), r(this).attr("data-password", "true"), r(this).addClass("show-password"))
                    : (r(this).siblings("input").attr("type", "password"), r(this).attr("data-password", "false"), r(this).removeClass("show-password"));
            }),
            r(".dropdown-menu a.dropdown-toggle").on("click", function (e) {
                return r(this).next().hasClass("show") || r(this).parents(".dropdown-menu").first().find(".show").removeClass("show"), r(this).next(".dropdown-menu").toggleClass("show"), !1;
            }),
            Waves.init(),
            feather.replace();
    }
    var t, n, o, a;
    e(),
        r(document).on("click", '.card a[data-bs-toggle="remove"]', function (e) {
            e.preventDefault();
            var t = r(this).closest(".card"),
                n = t.parent();
            t.remove(), 0 == n.children().length && n.remove();
        }),
        r(document).on("click", '.card a[data-bs-toggle="reload"]', function (e) {
            e.preventDefault();
            var t = r(this).closest(".card");
            t.append('<div class="card-disabled"><div class="card-portlets-loader"></div></div>');
            var n = t.find(".card-disabled");
            setTimeout(function () {
                n.fadeOut("fast", function () {
                    n.remove();
                });
            }, 500 + 5 * Math.random() * 300);
        }),
        r(".dropdown-menu a.dropdown-toggle").on("click", function () {
            var e = r(this).next(".dropdown-menu"),
                t = r(this).parent().parent().find(".dropdown-menu").not(e);
            return t.removeClass("show"), t.parent().find(".dropdown-toggle").removeClass("show"), !1;
        }),
        (t = r(".navbar-custom .dropdown:not(.app-search)")),
        r(document).on("click", function (e) {
            return "top-search" == e.target.id || e.target.closest("#search-dropdown") ? r("#search-dropdown").addClass("d-block") : r("#search-dropdown").removeClass("d-block"), !0;
        }),
        r("#top-search").on("focus", function (e) {
            return e.preventDefault(), t.children(".dropdown-menu.show").removeClass("show"), r("#search-dropdown").addClass("d-block"), !1;
        }),
        t.on("show.bs.dropdown", function () {
            r("#search-dropdown").removeClass("d-block");
        }),
        (n = document.querySelector('[data-toggle="fullscreen"]')) &&
            n.addEventListener("click", function (e) {
                e.preventDefault(),
                    document.body.classList.toggle("fullscreen-enable"),
                    document.fullscreenElement || document.mozFullScreenElement || document.webkitFullscreenElement
                        ? document.cancelFullScreen
                            ? document.cancelFullScreen()
                            : document.mozCancelFullScreen
                            ? document.mozCancelFullScreen()
                            : document.webkitCancelFullScreen && document.webkitCancelFullScreen()
                        : document.documentElement.requestFullscreen
                        ? document.documentElement.requestFullscreen()
                        : document.documentElement.mozRequestFullScreen
                        ? document.documentElement.mozRequestFullScreen()
                        : document.documentElement.webkitRequestFullscreen && document.documentElement.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
            }),
        r("[data-password]").on("click", function () {
            "false" == r(this).attr("data-password")
                ? (r(this).siblings("input").attr("type", "text"), r(this).attr("data-password", "true"), r(this).addClass("show-password"))
                : (r(this).siblings("input").attr("type", "password"), r(this).attr("data-password", "false"), r(this).removeClass("show-password"));
        }),
        document.querySelectorAll(".needs-validation").forEach(function (t) {
            t.addEventListener(
                "submit",
                function (e) {
                    t.checkValidity() || (e.preventDefault(), e.stopPropagation()), t.classList.add("was-validated");
                },
                !1
            );
        }),
        jQuery().select2 && r('[data-toggle="select2"]').select2(),
        jQuery().mask &&
            r('[data-toggle="input-mask"]').each(function (e, t) {
                var n = r(t).data("maskFormat"),
                    a = r(t).data("reverse");
                null != a ? r(t).mask(n, { reverse: a }) : r(t).mask(n);
            }),
        jQuery().daterangepicker &&
            ((o = {
                startDate: moment().subtract(29, "days"),
                endDate: moment(),
                ranges: {
                    Today: [moment(), moment()],
                    Yesterday: [moment().subtract(1, "days"), moment().subtract(1, "days")],
                    "Last 7 Days": [moment().subtract(6, "days"), moment()],
                    "Last 30 Days": [moment().subtract(29, "days"), moment()],
                    "This Month": [moment().startOf("month"), moment().endOf("month")],
                    "Last Month": [moment().subtract(1, "month").startOf("month"), moment().subtract(1, "month").endOf("month")],
                },
            }),
            r('[data-toggle="date-picker-range"]').each(function (e, t) {
                var n = r.extend({}, o, r(t).data()),
                    a = n.targetDisplay;
                r(t).daterangepicker(n, function (e, t) {
                    a && r(a).html(e.format("MMMM D, YYYY") + " - " + t.format("MMMM D, YYYY"));
                });
            }),
            (a = { cancelClass: "btn-light", applyButtonClasses: "btn-success" }),
            r('[data-toggle="date-picker"]').each(function (e, t) {
                var n = r.extend({}, a, r(t).data());
                r(t).daterangepicker(n);
            })),
        jQuery().timepicker &&
            ((a = { showSeconds: !0, icons: { up: "mdi mdi-chevron-up", down: "mdi mdi-chevron-down" } }),
            r('[data-toggle="timepicker"]').each(function (e, t) {
                var n = r.extend({}, a, r(t).data());
                r(t).timepicker(n);
            })),
        jQuery().TouchSpin &&
            ((a = {}),
            r('[data-toggle="touchspin"]').each(function (e, t) {
                var n = r.extend({}, a, r(t).data());
                r(t).TouchSpin(n);
            })),
        jQuery().maxlength &&
            ((a = { warningClass: "badge bg-success", limitReachedClass: "badge bg-danger", separator: " out of ", preText: "You typed ", postText: " chars available.", placement: "bottom" }),
            r('[data-toggle="maxlength"]').each(function (e, t) {
                var n = r.extend({}, a, r(t).data());
                r(t).maxlength(n);
            }));
})(jQuery);
var ThemeCustomizer = (function () {
    function e() {
        _classCallCheck(this, e), (this.html = document.getElementsByTagName("html")[0]), (this.config = {}), (this.defaultConfig = window.config), (this.mainNavScrollbar = document.getElementsByClassName("scrollbar")[0]);
    }
    return (
        _createClass(e, [
            {
                key: "initConfig",
                value: function () {
                    (this.defaultConfig = JSON.parse(JSON.stringify(window.defaultConfig))), (this.config = JSON.parse(JSON.stringify(window.config))), this.setSwitchFromConfig();
                },
            },
            {
                key: "initScrollBars",
                value: function () {
                    var e, t;
                    this.initLeftSidebar(),
                        null !== (e = document.querySelector(".app-menu .scrollbar")) && void 0 !== e && e.setAttribute("data-simplebar", ""),
                        null !== (t = document.querySelector(".app-menu .scrollbar")) && void 0 !== t && t.classList.add("h-100");
                },
            },
            {
                key: "initLeftSidebar",
                value: function () {
                    var n,
                        a,
                        t,
                        o,
                        r,
                        i = this;
                    $(".menu").length &&
                        ((o = $(".menu li .collapse")),
                        $(".menu li [data-bs-toggle='collapse']").on("click", function (e) {
                            return !1;
                        }),
                        o.on({
                            "show.bs.collapse": function (e) {
                                var t = $(e.target).parents(".collapse.show");
                                $(".menu .collapse.show").not(e.target).not(t).collapse("hide");
                            },
                        }),
                        $(".menu a").each(function () {
                            var e,
                                t,
                                n,
                                a = window.location.href.split(/[?#]/)[0];
                            this.href == a &&
                                ($(this).addClass("active"),
                                $(this).parent().addClass("menuitem-active"),
                                $(this).parent().parent().parent().addClass("show"),
                                $(this).parent().parent().parent().parent().addClass("menuitem-active"),
                                $(this).parent().parent().parent().parent().parent().parent().parent().addClass("menuitem-active"),
                                "sidebar-menu" !== (e = $(this).parent().parent().parent().parent().parent().parent()).attr("id") && e.addClass("show"),
                                "wrapper" !== (t = $(this).parent().parent().parent().parent().parent().parent().parent().parent().parent()).attr("id") && t.addClass("show"),
                                (n = $(this).parent().parent().parent().parent().parent().parent().parent().parent().parent().parent()).is("body") || n.addClass("menuitem-active"));
                        })),
                        $("#two-col-sidenav-main").length &&
                            ((n = $("#two-col-sidenav-main .menu-link")),
                            (a = $(".twocolumn-menu-item")),
                            (t = $(".twocolumn-menu-item .sub-menu")),
                            (o = $("#two-col-menu menu-item .collapse")).on({
                                "show.bs.collapse": function () {
                                    var e = $(this).closest(t).closest(t).find(o);
                                    e.length ? e.not($(this)).collapse("hide") : o.not($(this)).collapse("hide");
                                },
                            }),
                            n.on("click", function (e) {
                                var t = $($(this).attr("href"));
                                return t.length && (e.preventDefault(), n.removeClass("active"), $(this).addClass("active"), a.removeClass("d-block"), t.addClass("d-block"), 1040 <= window.innerWidth && i.changeLeftbarSize("default")), !0;
                            }),
                            (r = window.location.href),
                            n.each(function () {
                                this.href === r && $(this).addClass("active");
                            }),
                            $("#two-col-menu a").each(function () {
                                var e, t, n, a, o;
                                this.href == r &&
                                    ($(this).addClass("active"),
                                    $(this).parent().addClass("menuitem-active"),
                                    $(this).parent().parent().parent().addClass("show"),
                                    $(this).parent().parent().parent().parent().addClass("menuitem-active"),
                                    "sidebar-menu" !== (e = $(this).parent().parent().parent().parent().parent().parent()).attr("id") && e.addClass("show"),
                                    $(this).parent().parent().parent().parent().parent().parent().parent().addClass("menuitem-active"),
                                    "wrapper" !== (t = $(this).parent().parent().parent().parent().parent().parent().parent().parent().parent()).attr("id") && t.addClass("show"),
                                    (n = $(this).parent().parent().parent().parent().parent().parent().parent().parent().parent().parent()).is("body") || n.addClass("menuitem-active"),
                                    (a = null),
                                    (o = "#" + $(this).parents(".twocolumn-menu-item").attr("id")),
                                    $("#two-col-sidenav-main .menu-link").each(function () {
                                        $(this).attr("href") === o && (a = $(this));
                                    }),
                                    a && a.trigger("click"));
                            })),
                        setTimeout(function () {
                            var e,
                                t,
                                r,
                                n,
                                i,
                                c,
                                s,
                                l,
                                a = document.querySelector("li.menuitem-active .active");
                            null != a &&
                                ((e = document.querySelector(".app-menu .simplebar-content-wrapper")),
                                (t = a.offsetTop - 300),
                                e &&
                                    100 < t &&
                                    ((n = t),
                                    (i = 600),
                                    (c = (r = e).scrollTop),
                                    (s = n - c),
                                    (l = 0),
                                    (function e() {
                                        var t,
                                            n,
                                            a,
                                            o = ((t = l += 20), (n = c), (a = s), (t /= i / 2) < 1 ? (a / 2) * t * t + n : (-a / 2) * (--t * (t - 2) - 1) + n);
                                        (r.scrollTop = o), l < i && setTimeout(e, 20);
                                    })()));
                        }, 200);
                },
            },
            {
                key: "initHorizontalLayout",
                value: function () {
                    "horizontal" === html.getAttribute("data-layout") && 1040 < window.innerWidth && this.initLeftSidebar(!0);
                },
            },
            {
                key: "reverseQuery",
                value: function (e, t) {
                    for (; e; ) {
                        if (e.parentElement && e.parentElement.querySelector(t) === e) return e;
                        e = e.parentElement;
                    }
                    return null;
                },
            },
            {
                key: "changeThemeMode",
                value: function (e) {
                    (this.config.theme = e), this.html.setAttribute("data-bs-theme", e), this.setSwitchFromConfig();
                },
            },
            {
                key: "changeLayoutMode",
                value: function (e) {
                    this.html.setAttribute("data-layout-mode", e), (this.config.layout.mode = e), this.setSwitchFromConfig();
                },
            },
            {
                key: "changeLayoutWidth",
                value: function (e, t) {
                    var n = !(1 < arguments.length && void 0 !== t) || t;
                    this.html.setAttribute("data-layout-width", e), n && ((this.config.layout.width = e), this.setSwitchFromConfig());
                },
            },
            {
                key: "changeMenuIcon",
                value: function (e, t) {
                    var n = !(1 < arguments.length && void 0 !== t) || t;
                    this.html.setAttribute("data-menu-icon", e), n && ((this.config.menu.icon = e), this.setSwitchFromConfig());
                },
            },
            {
                key: "changeMenuColor",
                value: function (e) {
                    (this.config.menu.color = e), this.html.setAttribute("data-menu-color", e), this.setSwitchFromConfig();
                },
            },
            {
                key: "changeLeftbarSize",
                value: function (e, t) {
                    var n = !(1 < arguments.length && void 0 !== t) || t;
                    this.html.setAttribute("data-sidenav-size", e), n && ((this.config.sidenav.size = e), this.setSwitchFromConfig());
                },
            },
            {
                key: "changeTwocolumnColor",
                value: function (e) {
                    this.html.setAttribute("data-two-column-color", e), (this.config.sidenav.twocolumn = e), this.setSwitchFromConfig();
                },
            },
            {
                key: "changeTopbarColor",
                value: function (e) {
                    (this.config.topbar.color = e), this.html.setAttribute("data-topbar-color", e), this.setSwitchFromConfig();
                },
            },
            {
                key: "changeSidebarUser",
                value: function (e) {
                    (this.config.sidenav.user = e) ? this.html.setAttribute("data-sidenav-user", e) : this.html.removeAttribute("data-sidenav-user"), this.setSwitchFromConfig();
                },
            },
            {
                key: "resetTheme",
                value: function () {
                    (this.config = JSON.parse(JSON.stringify(window.defaultConfig))),
                        this.changeThemeMode(this.config.theme),
                        this.changeLayoutMode(this.config.layout.mode),
                        this.changeLayoutWidth(this.config.layout.width),
                        this.changeMenuColor(this.config.menu.color),
                        this.changeMenuIcon(this.config.menu.icon),
                        this.changeTopbarColor(this.config.topbar.color),
                        this.changeLeftbarSize(this.config.sidenav.size),
                        this.changeTwocolumnColor(this.config.sidenav.twocolumn),
                        this.adjustLayout();
                },
            },
            {
                key: "initSwitchListener",
                value: function () {
                    var n = this;
                    document.querySelectorAll("input[name=data-layout]").forEach(function (t) {
                        t.addEventListener("change", function (e) {
                            n.changeLayout(t.value);
                        });
                    }),
                        document.querySelectorAll("input[name=data-menu-color]").forEach(function (t) {
                            t.addEventListener("change", function (e) {
                                n.changeMenuColor(t.value);
                            });
                        }),
                        document.querySelectorAll("input[name=data-sidenav-size]").forEach(function (t) {
                            t.addEventListener("change", function (e) {
                                n.changeLeftbarSize(t.value);
                            });
                        }),
                        document.querySelectorAll("input[name=data-menu-icon]").forEach(function (t) {
                            t.addEventListener("change", function (e) {
                                n.changeMenuIcon(t.value);
                            });
                        }),
                        document.querySelectorAll("input[name=data-bs-theme]").forEach(function (t) {
                            t.addEventListener("change", function (e) {
                                n.changeThemeMode(t.value);
                            });
                        }),
                        document.querySelectorAll("input[name=data-layout-mode]").forEach(function (t) {
                            t.addEventListener("change", function (e) {
                                n.changeLayoutMode(t.value);
                            });
                        }),
                        document.querySelectorAll("input[name=data-layout-width]").forEach(function (t) {
                            t.addEventListener("change", function (e) {
                                n.changeLayoutWidth(t.value);
                            });
                        }),
                        document.querySelectorAll("input[name=data-topbar-color]").forEach(function (t) {
                            t.addEventListener("change", function (e) {
                                n.changeTopbarColor(t.value);
                            });
                        }),
                        document.querySelectorAll("input[name=data-two-column-color]").forEach(function (t) {
                            t.addEventListener("change", function (e) {
                                n.changeTwocolumnColor(t.value);
                            });
                        }),
                        document.querySelectorAll("input[name=data-sidebar-user]").forEach(function (t) {
                            t.addEventListener("change", function (e) {
                                n.changeSidebarUser(t.checked);
                            });
                        });
                    var e = document.getElementById("light-dark-mode");
                    e &&
                        e.addEventListener("click", function (e) {
                            "light" === n.config.theme ? n.changeThemeMode("dark") : n.changeThemeMode("light");
                        });
                    var t = document.querySelector("#reset-layout");
                    t &&
                        t.addEventListener("click", function (e) {
                            n.resetTheme();
                        });
                    var a = document.querySelector(".button-toggle-menu");
                    a &&
                        a.addEventListener("click", function () {
                            var e = n.config.sidenav.size,
                                t = n.html.getAttribute("data-sidenav-size", e);
                            "full" === t
                                ? n.showBackdrop()
                                : "fullscreen" == e
                                ? "fullscreen" === t
                                    ? n.changeLeftbarSize("fullscreen" == e ? "default" : e, !1)
                                    : n.changeLeftbarSize("fullscreen", !1)
                                : "condensed" === t
                                ? n.changeLeftbarSize("condensed" == e ? "default" : e, !1)
                                : n.changeLeftbarSize("condensed", !1),
                                n.html.classList.toggle("sidebar-enable");
                        }),
                        document.querySelectorAll(".button-sm-hover").forEach(function (e) {
                            e.addEventListener("click", function () {
                                var e = n.config.sidenav.size;
                                "sm-hover-active" === n.html.getAttribute("data-sidenav-size", e) ? n.changeLeftbarSize("sm-hover", !1) : n.changeLeftbarSize("sm-hover-active", !1);
                            });
                        });
                },
            },
            {
                key: "showBackdrop",
                value: function () {
                    var e,
                        t = document.createElement("div");
                    (t.id = "custom-backdrop"),
                        (t.classList = "offcanvas-backdrop fade show"),
                        document.body.appendChild(t),
                        "rtl" != (null === (e = document.getElementsByTagName("html")[0]) || void 0 === e ? void 0 : e.getAttribute("dir")) &&
                            ((document.body.style.overflow = "hidden"), 1140 < window.innerWidth && (document.body.style.paddingRight = "15px"));
                    var n = this;
                    t.addEventListener("click", function (e) {
                        n.html.classList.remove("sidebar-enable"), n.hideBackdrop();
                    });
                },
            },
            {
                key: "hideBackdrop",
                value: function () {
                    var e = document.getElementById("custom-backdrop");
                    e && (document.body.removeChild(e), (document.body.style.overflow = null), (document.body.style.paddingRight = null));
                },
            },
            {
                key: "initWindowSize",
                value: function () {
                    var t = this;
                    window.addEventListener("resize", function (e) {
                        t.adjustLayout();
                    });
                },
            },
            {
                key: "adjustLayout",
                value: function () {
                    window.innerWidth <= 1140 ? this.changeLeftbarSize("full", !1) : this.changeLeftbarSize(this.config.sidenav.size);
                },
            },
            {
                key: "setSwitchFromConfig",
                value: function () {
                    sessionStorage.setItem("__UBOLD_CONFIG__", JSON.stringify(this.config)),
                        document.querySelectorAll(".right-bar input[type=checkbox]").forEach(function (e) {
                            e.checked = !1;
                        });
                    var e,
                        t,
                        n,
                        a,
                        o,
                        r,
                        i,
                        c,
                        s,
                        l = this.config;
                    l &&
                        ((e = document.querySelector("input[type=checkbox][name=data-bs-theme][value=" + l.theme + "]")),
                        (t = document.querySelector("input[type=checkbox][name=data-layout-mode][value=" + l.layout.mode + "]")),
                        (n = document.querySelector("input[type=checkbox][name=data-layout-width][value=" + l.layout.width + "]")),
                        (a = document.querySelector("input[type=checkbox][name=data-topbar-color][value=" + l.topbar.color + "]")),
                        (o = document.querySelector("input[type=checkbox][name=data-menu-color][value=" + l.menu.color + "]")),
                        (r = document.querySelector("input[type=checkbox][name=data-menu-icon][value=" + l.menu.icon + "]")),
                        (i = document.querySelector("input[type=checkbox][name=data-sidenav-size][value=" + l.sidenav.size + "]")),
                        (c = document.querySelector("input[type=checkbox][name=data-two-column-color][value=" + l.sidenav.twocolumn + "]")),
                        (s = document.querySelector("input[type=checkbox][name=data-sidebar-user]")),
                        e && (e.checked = !0),
                        t && (t.checked = !0),
                        n && (n.checked = !0),
                        a && (a.checked = !0),
                        o && (o.checked = !0),
                        r && (r.checked = !0),
                        i && (i.checked = !0),
                        c && (c.checked = !0),
                        s && "true" === l.sidenav.user.toString() && (s.checked = !0));
                },
            },
            {
                key: "init",
                value: function () {
                    this.initConfig(), this.initScrollBars(), this.initLeftSidebar(), this.initSwitchListener(), this.initWindowSize(), this.adjustLayout(), this.setSwitchFromConfig();
                },
            },
        ]),
        e
    );
})();
new ThemeCustomizer().init();
