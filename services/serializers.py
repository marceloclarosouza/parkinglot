from rest_framework import serializers
from .models import Client, Service, Order, Feedback
from cpf_field.models import CPFField
from datetime import datetime

class ClientSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=200)
    cpf = CPFField(unique=True)

    class Meta:
        model = Client
        fields = ('__all__')

class ServiceSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=10)
    service = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    
    class Meta:
        model = Service
        fields = ('__all__')

class OrderSerializer(serializers.ModelSerializer):
    service_date = serializers.DateTimeField(default=datetime.now)

    class Meta:
        model = Order
        fields = ('__all__')

class FeedbackSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=30)
    feedback = serializers.CharField(max_length=200)
    feedback_date = serializers.DateTimeField(default=datetime.now)
    
    class Meta:
        model = Feedback
        fields = ('__all__')