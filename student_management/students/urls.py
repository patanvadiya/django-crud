from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('new/', views.student_create, name='student_create'),
    path('edit/<int:id>/', views.student_edit, name='student_edit'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),  
    path('view/<int:id>/', views.student_image, name='student_image'),  

]