"""
URL configuration for studentregistration project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.show),
    path('reg/', views.register, name='register'),
    path('all_students/', views.all_students, name='all_students'),
    path('delete_stud/', views.delete_student, name='delete_student'),
    path('delete_stud/<int:student_id>/', views.delete_student, name='delete_stud'),
    path('update_student/<int:id>/', views.update_student, name='update_student'), 
    path('student_update/<int:id>/', views.student_update, name='student_update'),
]

