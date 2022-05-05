from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=200)
    cpf = models.IntegerField(max_length=11, unique=True)

    def __str__(self):
        return self.first_name

class Service(models.Model):
    cpf = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.CharField(max_length=200)
    price = models.FloatField()
    service_date = models.DateTimeField()

    def __str__(self):
        return self.service

class Evaluation(models.Model):
    cpf = models.ForeignKey(Client, on_delete=models.CASCADE)
    comments = models.CharField(max_length=200)

    def __str__(self):
        return self.comments

