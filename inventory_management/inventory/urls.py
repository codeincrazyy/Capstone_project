from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, InventoryChangeViewSet

router = DefaultRouter()
router.register(r'items', InventoryItemViewSet, basename='item')
router.register(r'changes', InventoryChangeViewSet, basename='change')

urlpatterns = router.urls
