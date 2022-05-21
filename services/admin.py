from django.contrib import admin
from import_export.admin import ImportExportMixin

from .models import Client, Feedback, Order, Services

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cpf', 'email')
    list_filter = ('cpf', 'email')
    search_fields = ('cpf', 'email')
        
    class Meta:
        model = Client
    

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('code', 'service', 'price')
    list_filter = ('service',)
    search_fields = ('service__name',)

    class Meta:
        model = Services
    

class OrderAdmin(admin.ModelAdmin):
    list_display = ('service', 'price', 'service_date')
    list_filter = ('service_date',)
    search_filed = ('service__name', 'cpf')

    class Meta:
        model = Order

class FeedbackAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('service','feedback', 'name', 'feedback_date')
    list_filter = ('feedback_date',)
    search_field = ('service__name', )    

    class Meta:
        model = Feedback        
    

admin.site.register(Client, ClientAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Feedback, FeedbackAdmin)
