from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL  # default 'auth.User'

class InventoryItem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.quantity})"

class InventoryChange(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE, related_name='changes')
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    old_quantity = models.PositiveIntegerField()
    new_quantity = models.PositiveIntegerField()
    reason = models.CharField(max_length=255, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']
