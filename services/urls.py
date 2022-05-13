from django.urls import path

from . import views

app_name = 'services'

urlpatterns = [
    path('', views.index, name='index'),
    path('feedback/', views.get_feedback, name='feedback'),
    path('service/', views.get_services, name='service')
]
