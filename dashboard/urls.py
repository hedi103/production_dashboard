from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('lissage', views.lissage, name='lissage'),
    path('decalage_prod', views.decalage_prod, name='decalage_prod'),
    path('regulation_freq', views.regulation_freq, name='regulation_freq')
]