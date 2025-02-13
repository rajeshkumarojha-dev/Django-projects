
from django.urls import path,include
from . import views
from django.contrib.auth.urls import views as auth_views


urlpatterns = [
    path('',views.home,name='home'),
    path('list/',views.emp_list,name='list'),
    path('add/',views.emp_form,name='add'),
    path('update/<id>/',views.update_emp,name='update'),
    path('delete/<id>/',views.delete_emp,name='delete'),
    path('api/emp/',views.employee_api,name='api'),
    path('api/emp/<id>/',views.employee_api),
    path('accounts/',include('django.contrib.auth.urls')),

    path('signin/',views.signin_request,name='signin'),
    path('login/',views.login_request,name='login'),
    path('logout/',views.logout_request,name='logout'),
    
]