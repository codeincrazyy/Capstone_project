from rest_framework import viewsets, filters, generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from .models import InventoryItem, InventoryChange
from .serializers import InventoryItemSerializer, InventoryChangeSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from .filters import InventoryItemFilter


User = get_user_model()

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all().select_related('owner')
    serializer_class = InventoryItemSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'quantity', 'price', 'date_added']
    filterset_class = InventoryItemFilter
    
    def perform_create(self, serializer):
        item = serializer.save(owner=self.request.user)
        # Log initial quantity change from 0 to provided value
        InventoryChange.objects.create(
            item=item,
            changed_by=self.request.user,
            old_quantity=0,
            new_quantity=item.quantity,
            reason='Initial add'
        )

    def perform_update(self, serializer):
        instance = self.get_object()
        old_qty = instance.quantity
        item = serializer.save()
        new_qty = item.quantity
        if old_qty != new_qty:
            InventoryChange.objects.create(
                item=item,
                changed_by=self.request.user,
                old_quantity=old_qty,
                new_quantity=new_qty,
                reason='Quantity update via API'
            )

class InventoryChangeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = InventoryChange.objects.all().select_related('item', 'changed_by')
    serializer_class = InventoryChangeSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['item']
    ordering_fields = ['timestamp']

class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # This automatically hashes the password securely
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]  # anyone can register
    serializer_class = RegisterSerializer