from django.urls import path, include
from .views import index, go

urlpatterns = [
    path('', index, name='home'),
    # path('create', create, name='create'),
    path('<str:pk>', go, name='go'),
]
