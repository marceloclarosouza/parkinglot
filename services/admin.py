from django.contrib import admin

from .models import Client, Market, Service, Evaluation

admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Market)
admin.site.register(Evaluation)


