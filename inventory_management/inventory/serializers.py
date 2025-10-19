from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import InventoryItem, InventoryChange

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class InventoryItemSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)

    class Meta:
        model = InventoryItem
        fields = ['id', 'owner', 'name', 'description', 'quantity', 'price', 'category', 'date_added', 'last_updated']
        read_only_fields = ['id', 'owner', 'date_added', 'last_updated']

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value

class InventoryChangeSerializer(serializers.ModelSerializer):
    changed_by = UserSerializer(read_only=True)

    class Meta:
        model = InventoryChange
        fields = ['id', 'item', 'changed_by', 'old_quantity', 'new_quantity', 'reason', 'timestamp']
        read_only_fields = ['id', 'changed_by', 'timestamp']
