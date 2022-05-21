from django.urls import path
# from django.conf.urls import url
from .views import ClientViews, FeedbackViews, OrderViews, ServicesViews

from . import views

app_name = 'services'

urlpatterns = [
    path('feedback/', views.feedback_form, name='feedback'),
    path('feedback-api/', FeedbackViews.as_view()),
    path('feedback-api/<int:id>', FeedbackViews.as_view()),
    path('client-api/', ClientViews.as_view()),
    path('client-api/<int:id>', ClientViews.as_view()),
    path('service-api/', ServicesViews.as_view()),
    path('service-api/<int:id>', ServicesViews.as_view()),
    path('order-api/', OrderViews.as_view()),
    path('order-api/<int:id>', OrderViews.as_view()),    
]
