from django.contrib import admin
from .models import Record, Lead, SalesMember

admin.site.register(Record)
admin.site.register(Lead)
admin.site.register(SalesMember)