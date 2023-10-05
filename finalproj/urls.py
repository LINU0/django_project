"""finalproj URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from fpsite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userinfo/', views.userinfo),
    path('accounts/', include('registration.backends.default.urls')),
    path("booking/",views.booking),
    path("login/",views.login),
    path("logout/",views.logout),
    path('addphoto/',views.addphoto),
    path('seeuser/',views.seeuser),
    path('seeuser/<int:pid>',views.seeuser),
    path('roomdetail/<str:r>',views.roomdetail,name = 'roomdetail-url'),
    path('check_book/',views.check_book),
    path('electric/',views.electric),
    path('adminelectric/',views.adminelectric),
    path('adminelectric/<str:rnum>',views.adminelectric),
    path('electinfo/', views.electinfo),
    path('', views.index),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
