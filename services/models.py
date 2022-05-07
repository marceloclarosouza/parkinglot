from django.db import models
from cpf_field.models import CPFField

class Client(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=200, null=False, blank=False)
    cpf = CPFField(unique=True, null=False, blank=False)

    def __str__(self):
        return self.first_name

class Service(models.Model):
    code = models.CharField(max_length=10, unique=True, null=False, blank=False)
    service = models.CharField(max_length=200, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    
    def __str__(self):
        return self.service

class Market(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    cpf = models.ForeignKey(Client, on_delete=models.CASCADE)
    service_date = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return str(self.service)

class Evaluation(Market):
    comments = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.comments

