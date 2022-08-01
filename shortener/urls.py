from django.urls import path
from .views import index, go


app_name = 'shortener'
urlpatterns = [
    path('', index, name='home'),
    path('<str:pk>', go, name='go'),
]
