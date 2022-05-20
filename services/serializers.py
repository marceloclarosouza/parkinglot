from rest_framework import serializers
from .models import Client, Services, Order, Feedback
from cpf_field.models import CPFField
from datetime import datetime

class ClientSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=200)
    cpf = CPFField(unique=True)
    email = serializers.EmailField()

    class Meta:
        model = Client
        fields = ('__all__')

class ServicesSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=10)
    service = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    
    class Meta:
        model = Services
        fields = ('__all__')

class OrderSerializer(serializers.ModelSerializer):
    service = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    cpf = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    service_date = serializers.DateTimeField(default=datetime.now)
    quantity = serializers.IntegerField(default=1)
    price = serializers.FloatField(read_only=True)

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