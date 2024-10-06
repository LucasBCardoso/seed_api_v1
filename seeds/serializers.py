from rest_framework import serializers
from seeds.models import User, UserCargo, UserProfile, Client, UserCheckIn, ClientAddress, ClientContact, ClientMail, ClientPhone, NegotiationStatus, ClientNegotiation, OrderStatus, PaymentMethods, OrderShipping, Order, Culture, Variety, Packing, OrderBatch, OrderBatchPacking, OrderItems, OrderBatchRelation, Tsi


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCargo
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class UserCheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCheckIn
        fields = '__all__'


class ClientAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientAddress
        fields = '__all__'


class ClientContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContact
        fields = '__all__'


class ClientMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientMail
        fields = '__all__'


class ClientPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientPhone
        fields = '__all__'


class NegotiationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = NegotiationStatus
        fields = '__all__'


class ClientNegotiationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientNegotiation
        fields = '__all__'


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'


class OrderShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderShipping
        fields = '__all__'


class PaymentMethodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethods
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Culture
        fields = '__all__'


class VarietySerializer(serializers.ModelSerializer):
    class Meta:
        model = Variety
        fields = '__all__'


class OrderBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBatch
        fields = '__all__'


class OrderBatchPackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBatchPacking
        fields = '__all__'


class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'


class OrderBatchRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderBatchRelation
        fields = '__all__'


class PackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packing
        fields = '__all__'


class TsiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tsi
        fields = '__all__'