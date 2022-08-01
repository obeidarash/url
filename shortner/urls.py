from django.urls import path, include
from .views import index, go


app_name = 'shortener'
urlpatterns = [
    path('', index, name='home'),
    # path('create', create, name='create'),
    path('<str:pk>', go, name='go'),
]
