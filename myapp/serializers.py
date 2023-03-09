from rest_framework import serializers
from .models import Receipt
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    receipts = serializers.PrimaryKeyRelatedField(many=True, queryset=Receipt.objects.all())

    class Meta:
        model = User
        fields = ("id", "username", "receipts")

class ReceiptSerializer(serializers.ModelSerializer):
    
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Receipt
        fields = ("issue_date", "price_per_liter", "total_value", "calculate_tax_value", "calculate_net_value", "calculate_liters")