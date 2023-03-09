from rest_framework import serializers
from .models import Receipt

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ("issue_date", "price_per_liter", "total_value", "calculate_tax_value", "calculate_net_value", "calculate_liters")