from django.urls import path
from .import views

urlpatterns = [
    path('add/', views.add_employee_view, name = 'add_url'),
    path('show/', views.show_employee_view, name = 'show_url'),
    path('update/<pk>', views.update_employee_view, name = 'update_url'),
    path('delete/<pk>', views.delete_employee_view, name = 'delete_url')
]