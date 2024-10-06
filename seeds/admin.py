from django.contrib import admin
from seeds.models import User, UserCargo, UserProfile, Client, UserCheckIn, ClientAddress, ClientContact, ClientMail, ClientPhone, NegotiationStatus, ClientNegotiation, OrderStatus, OrderShipping, PaymentMethods, Order, Culture, Variety, OrderBatch, OrderBatchPacking, OrderItems, OrderBatchRelation, Packing, Tsi


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'created_at')
    search_fields = ('username', 'email',)


class UserCargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_user_name', 'get_cargo_name', 'email', 'created_at')
    search_fields = ('user_id__username', 'cargo__name', 'email',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'fantasy_name', 'company_name', 'cpf_cnpj', 'created_at')
    search_fields = ('fantasy_name', 'cpf_cnpj',)


class UserCheckInAdmin(admin.ModelAdmin):
    list_display = ('id', 'latitude', 'longitude', 'get_client_name', 'created_at')
    search_fields = ('client_id__fantasy_name',)


class ClientAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'street', 'number', 'neighborhood', 'city', 'complement', 'state_abbreviation', 'created_at')
    search_fields = ('street', 'number', 'neighborhood', 'city', 'complement', 'state_abbreviation',)


class ClientContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_client_name', 'created_at')
    search_fields = ('client_id__fantasy_name',)


class ClientMailAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_id', 'email', 'created_at')
    search_fields = ('contact_id', 'email',)


class ClientPhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact_id', 'phone_number', 'created_at')
    search_fields = ('contact_id', 'phone_number',)


class NegotiationStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


class ClientNegotiationAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_client_name', 'created_at')
    search_fields = ('client_id__fantasy_name',)


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


class OrderSippingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


class PaymentMethodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'shipping', 'get_client_name', 'created_at')
    search_fields = ('name', 'shipping', 'client_id__fantasy_name',)


class CultureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


class VarietyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_culture_name', 'created_at')
    search_fields = ('name', 'culture_id__name',)


class OrderBatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'germination', 'purity', 'approved', 'premium', 'created_at')
    search_fields = ('name', 'germination',)


class OrderBatchPackingAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_batch_name', 'get_packing_name', 'created_at')
    search_fields = ('batch_id__name', 'packing_id__name')


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_order_name', 'get_culture_name', 'get_variety_name', 'get_batch_name', 'packing_id', 'created_at')
    search_fields = ('item_culture__name', 'item_variety__name', 'order_id__name', 'batch_id__name',)


class OrderBatchRelationAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_order_name', 'get_batch_name', 'total_price', 'created_at')
    search_fields = ('get_order_name',)


class PackingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


class TsiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    search_fields = ('name',)


admin.site.register(User, UserAdmin)
admin.site.register(UserCargo, UserCargoAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(UserCheckIn, UserCheckInAdmin)
admin.site.register(ClientAddress, ClientAddressAdmin)
admin.site.register(ClientContact, ClientContactAdmin)
admin.site.register(ClientMail, ClientMailAdmin)
admin.site.register(ClientPhone, ClientPhoneAdmin)
admin.site.register(NegotiationStatus, NegotiationStatusAdmin)
admin.site.register(ClientNegotiation, ClientNegotiationAdmin)
admin.site.register(OrderStatus, OrderStatusAdmin)
admin.site.register(OrderShipping, OrderSippingAdmin)
admin.site.register(PaymentMethods, PaymentMethodsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Culture, CultureAdmin)
admin.site.register(Variety, VarietyAdmin)
admin.site.register(OrderBatch, OrderBatchAdmin)
admin.site.register(OrderBatchPacking, OrderBatchPackingAdmin)
admin.site.register(OrderItems, OrderItemsAdmin)
admin.site.register(OrderBatchRelation, OrderBatchRelationAdmin)
admin.site.register(Packing, PackingAdmin)
admin.site.register(Tsi, TsiAdmin)