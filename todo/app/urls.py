from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('todo/',views.todo_request,name='todo'),
    path('delete/<int:id>/',views.delete_request,name='delete'),
    path('update/<int:id>/',views.update_request,name='update'),
    path('list/',views.list_request,name='list'),
    path('signin/',views.SignIn_request, name='signin'),
    path('login/',views.login_request, name='login'),
    path('logout/',views.logout_request, name='logout'),
]