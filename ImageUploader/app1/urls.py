
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import home,view_images,image_delete,image_edit
urlpatterns = [
    path('',home,name='home'),
    path('view/',view_images,name='view'),
    path('delete/<id>/',image_delete,name='delete'),
    path('update/<id>/',image_edit,name='update'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)