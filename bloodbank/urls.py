"""bloodbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import donarapp
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('donarapp.urls')),
    path('register/',include('donarapp.urls')),
    path('login/',include('donarapp.urls')),
    path('logout/',include('donarapp.urls')),
    path('main/',include('donarapp.urls')),
    path('donar/',include('donarapp.urls')),
    path('complete/',include('donarapp.urls')),
    path('search/',include('donarapp.urls')),
    path('search_value/',include('donarapp.urls')),
    path('account/',include('donarapp.urls')),
    path('address/',include('donarapp.urls')),
    path('phone/',include('donarapp.urls')),
    path('address_return/',include('donarapp.urls')),
    path('phone_return/',include('donarapp.urls'))

]

