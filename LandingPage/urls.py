from django.urls import path
from .views import index
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('contacto/', views.send_contact_email, name='contacto'),
]