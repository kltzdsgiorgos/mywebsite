from django.contrib import admin

from . models import Receipt

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("issue_date", "price_per_liter", "total_value", "calculate_tax_value", "calculate_net_value", "calculate_liters")
