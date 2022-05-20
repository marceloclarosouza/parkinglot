from django.db import models
from cpf_field.models import CPFField
from datetime import datetime

class Client(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    cpf = CPFField(unique=True, null=False, blank=False)
    email = models.EmailField(null=False, blank=False, unique=True)

    def register(self):
        self.save()

    @staticmethod
    def get_client_by_email(email):
        return Client.objects.get(email=email)

    def is_exists(self):
        if Client.objects.filter(email=self.email):
            return True
        return False

    def __str__(self):
        return self.first_name

class Services(models.Model):
    code = models.CharField(max_length=10, unique=True, null=False, blank=False)
    service = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

    @staticmethod
    def get_services_by_id(id):
        return Services.objects.filter(id__in=id)

    @staticmethod
    def get_all_services():
        return Services.objects.all()
    
    def __str__(self):
        return self.service

class Order(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    cpf = models.ForeignKey(Client, on_delete=models.CASCADE)
    service_date = models.DateTimeField(default=datetime.now, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

    def place_order(self):
        self.save()

    @staticmethod
    def get_orders_by_client(cpf_id):
        return Order.objects.filter(cpf=cpf_id).order_by('-date')

    @staticmethod
    def get_all_orders():
        return Order.objects.all().order_by('-date')

    def __str__(self):
        return str(self.service)

class Feedback(models.Model):
    name = models.CharField(max_length=30, blank=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=200, null=False, blank=False)
    feedback_date = models.DateTimeField(default=datetime.now, null=False, blank=False)

    def register(self):
        self.save()

    @staticmethod
    def get_feedback_by_client(id):
        return Feedback.objects.filter(id=id)

    @staticmethod
    def get_all_feedback():
        return Feedback.objects.all().order_by('-date')
    
    def __str__(self):
        return self.feedback
