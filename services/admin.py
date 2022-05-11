from django.contrib import admin

from .models import Client, Feedback, Order, Service


class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('first_name', 'last_name', 'cpf')

class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ('code', 'service', 'price')

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('service', 'service_date', 'cpf')

class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = ('feedback', 'name')


admin.site.register(Client, ClientAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Feedback, FeedbackAdmin)