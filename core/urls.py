from django.urls import path
from .views import number_properties_view

urlpatterns = [
    path('classify-number', number_properties_view, name='number_properties'),
]
