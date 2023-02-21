
from django.contrib import admin
from django.urls import path
from employee import views


urlpatterns = [
    path('', views.show, name='show'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('add/', views.add, name='add'),
]
