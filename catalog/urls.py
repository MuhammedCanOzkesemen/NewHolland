from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tractors/', views.series_list, name='series_list'),
    path('tractors/<slug:slug>/', views.series_detail, name='series_detail'),
    path('models/<slug:slug>/', views.model_detail, name='model_detail'),
    path('iletisim/', views.contact, name='contact'),
]
