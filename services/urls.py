from django.urls import path
from .views import ClientViews, FeedbackViews, OrderViews, ServiceViews

from . import views

app_name = 'services'

urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('service/', views.ServicesView.as_view(), name='service'),
    # path('feedback/', views.FeedbackView.as_view(), name='feedback'),
    path('feedback-api/', FeedbackViews.as_view()),
    path('feedback-api/<int:id>', FeedbackViews.as_view()),
    path('client-api/', ClientViews.as_view()),
    path('client-api/<int:id>', ClientViews.as_view()),
    path('service-api/', ServiceViews.as_view()),
    path('service-api/<int:id>', ServiceViews.as_view()),
    # path('order-api/', OrderViews),
    # path('order-api/<int:id>', OrderViews),
    
]
