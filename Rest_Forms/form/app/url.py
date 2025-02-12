
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('list/',views.emp_list,name='list'),
    path('add/',views.emp_form,name='add'),
    path('update/<id>/',views.update_emp,name='update'),
    path('delete/<id>/',views.delete_emp,name='delete'),
    path('api/emp/',views.employee_api,name='api'),
    path('api/emp/<id>/',views.employee_api),
]