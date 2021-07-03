from django.contrib import admin
from django.contrib.auth import login
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('login/',views.logins),
    path('logout/',views.logsout),
    path('main/',views.main,name="welcome"),
    path('donar/',views.donar),
    path('complete/',views.complete),
    path('search/',views.search),
    path('search_value/',views.search_value),
    path('account/',views.account,name="account"),
    path('address/',views.address),
    path('phone/',views.phone),
    path('address_return/',views.address_return),
    path('phone_return/',views.phone_return),

]

urlpatterns+= staticfiles_urlpatterns()