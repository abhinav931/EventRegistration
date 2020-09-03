from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.Registration, name = 'register'),
    path('success/', views.Success, name = 'success'),
    path('update_tables/', views.UpdateTables, name = 'update_tables'),
   
]