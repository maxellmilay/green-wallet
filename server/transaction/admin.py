from django.contrib import admin
from .models import TransactionGroup, Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('name','group','amount')
    list_filter = ['group']
    search_fields = ['name']

class TransactionGroupAdmin(admin.ModelAdmin):
    list_display = ('name','owner')

admin.site.register(TransactionGroup, TransactionGroupAdmin)
admin.site.register(Transaction, TransactionAdmin)
