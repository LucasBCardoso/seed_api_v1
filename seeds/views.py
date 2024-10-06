from rest_framework import viewsets
#from dj_rql.drf import RQLFilterBackend
#from seeds.filters import UserFilter, UserProfileFilter, ClientFilter, UserCheckInFilter, ClientAddressFilter, ClientContactFilter, ClientMailFilter, ClientPhoneFilter, ClientNegotiationFilter, OrderFilter, CultureFilter, VarietyFilter, OrderBatchFilter, OrderBatchPackingFilter, OrderItemsFilter
from seeds.models import User, UserCargo, UserProfile, Client, UserCheckIn, ClientAddress, ClientContact, ClientMail, ClientPhone, NegotiationStatus, ClientNegotiation, OrderStatus, OrderStatus, OrderShipping, PaymentMethods, Order, Culture, Variety, OrderBatch, OrderBatchPacking, OrderItems, OrderBatchRelation, Packing, Tsi
from seeds.serializers import UserSerializer, UserCargoSerializer, UserProfileSerializer, ClientSerializer, UserCheckInSerializer, ClientAddressSerializer, ClientContactSerializer, ClientMailSerializer, ClientPhoneSerializer, NegotiationStatusSerializer, ClientNegotiationSerializer, OrderStatusSerializer, OrderShippingSerializer, PaymentMethodsSerializer, OrderSerializer, CultureSerializer, VarietySerializer, OrderBatchSerializer, OrderBatchPackingSerializer, OrderItemsSerializer, OrderBatchRelationSerializer, PackingSerializer, TsiSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #filter_backends = [RQLFilterBackend]
    #rql_filter_class = UserFilter


class UserCargoViewSet(viewsets.ModelViewSet):
    queryset = UserCargo.objects.all()
    serializer_class = UserCargoSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class UserCheckInViewSet(viewsets.ModelViewSet):
    queryset = UserCheckIn.objects.all()
    serializer_class = UserCheckInSerializer


class ClientAddressViewSet(viewsets.ModelViewSet):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressSerializer


class ClientContactViewSet(viewsets.ModelViewSet):
    queryset = ClientContact.objects.all()
    serializer_class = ClientContactSerializer


class ClientMailViewSet(viewsets.ModelViewSet):
    queryset = ClientMail.objects.all()
    serializer_class = ClientMailSerializer


class ClientPhoneViewSet(viewsets.ModelViewSet):
    queryset = ClientPhone.objects.all()
    serializer_class = ClientPhoneSerializer


class NegotiationStatusViewSet(viewsets.ModelViewSet):
    queryset = NegotiationStatus.objects.all()
    serializer_class = NegotiationStatusSerializer


class ClientNegotiationViewSet(viewsets.ModelViewSet):
    queryset = ClientNegotiation.objects.all()
    serializer_class = ClientNegotiationSerializer


class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer


class OrderShippingViewSet(viewsets.ModelViewSet):
    queryset = OrderShipping.objects.all()
    serializer_class = OrderShippingSerializer


class PaymentMethodsViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethods.objects.all()
    serializer_class = PaymentMethodsSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CultureViewSet(viewsets.ModelViewSet):
    queryset = Culture.objects.all()
    serializer_class = CultureSerializer


class VarietyViewSet(viewsets.ModelViewSet):
    queryset = Variety.objects.all()
    serializer_class = VarietySerializer


class OrderBatchViewSet(viewsets.ModelViewSet):
    queryset = OrderBatch.objects.all()
    serializer_class = OrderBatchSerializer


class OrderBatchPackingViewSet(viewsets.ModelViewSet):
    queryset = OrderBatchPacking.objects.all()
    serializer_class = OrderBatchPackingSerializer


class OrderItemsViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemsSerializer


class OrderBatchRelationViewSet(viewsets.ModelViewSet):
    queryset = OrderBatchRelation.objects.all()
    serializer_class = OrderBatchRelationSerializer


class PackingViewSet(viewsets.ModelViewSet):
    queryset = Packing.objects.all()
    serializer_class = PackingSerializer


class TsiViewSet(viewsets.ModelViewSet):
    queryset = Tsi.objects.all()
    serializer_class = TsiSerializer