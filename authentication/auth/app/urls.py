
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/emp/', views.emp_api, name='emp_api'),
    path('list/', views.emp_list, name='emp_list'),
    path('update/<int:id>/', views.update_emp, name='update_emp'),
    path('delete/<int:id>/', views.delete_emp, name='delete_emp'),
    # Add other paths here
]