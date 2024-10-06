from django.urls import path, include
from rest_framework.routers import DefaultRouter
from seeds.views import UserViewSet, UserCargoViewSet, UserProfileViewSet, ClientViewSet, UserCheckInViewSet, ClientAddressViewSet, ClientContactViewSet, ClientMailViewSet, ClientPhoneViewSet, NegotiationStatusViewSet, ClientNegotiationViewSet, OrderStatusViewSet, OrderShippingViewSet, PaymentMethodsViewSet, OrderViewSet, CultureViewSet, VarietyViewSet, OrderBatchViewSet, OrderBatchPackingViewSet, OrderItemsViewSet, OrderBatchRelationViewSet, PackingViewSet, TsiViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'user-cargo', UserCargoViewSet)
router.register(r'user-profile', UserProfileViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'user-checkin', UserCheckInViewSet)
router.register(r'client-address', ClientAddressViewSet)
router.register(r'client-contact', ClientContactViewSet)
router.register(r'client-mail', ClientMailViewSet)
router.register(r'client-phone', ClientPhoneViewSet)
router.register(r'negotiation-status', NegotiationStatusViewSet)
router.register(r'client-negotiation', ClientNegotiationViewSet)
router.register(r'order-status', OrderStatusViewSet)
router.register(r'order-shipping', OrderShippingViewSet)
router.register(r'payment-methods', PaymentMethodsViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'cultures', CultureViewSet)
router.register(r'varieties', VarietyViewSet)
router.register(r'order-batches', OrderBatchViewSet)
router.register(r'order-batch-packing', OrderBatchPackingViewSet)
router.register(r'order-items', OrderItemsViewSet)
router.register(r'order-batch-relation', OrderBatchRelationViewSet)
router.register(r'packings', PackingViewSet)
router.register(r'tsi', TsiViewSet)


urlpatterns = [
    path('', include(router.urls)),
]