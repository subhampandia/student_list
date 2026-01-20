"""
URL configuration for project3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_list/', student_list, name='student_list'),
    path('student_add/', student_add, name='student_add'),
    path('student_update/<int:id>/', student_update, name='student_update'),
    path('student_delete/<int:id>/', student_delete, name='student_delete'),

]

if settings.DEBUG : 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)