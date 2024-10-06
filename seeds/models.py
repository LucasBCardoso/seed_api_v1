from django.db import models
from django.db.models import Q
#from django.contrib.auth.models import User


class User(models.Model): #Usuários
    id = models.AutoField(primary_key=True, verbose_name="ID")  # Assuming id is an auto-increment integer field
    username = models.CharField(max_length=255, unique=True, verbose_name='Nome de usuário')
    password = models.CharField(max_length=255, verbose_name='Senha')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def __str__(self):
        return str(self.username)
    
    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


class UserCargo(models.Model): #Cargos
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Nome")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"


class UserProfile(models.Model): #Perfil
    id = models.AutoField(primary_key=True, verbose_name="ID")
    works_at = models.CharField(max_length=255, verbose_name="Local de Trabalho")
    email = models.EmailField(unique=True, verbose_name="Email")
    registration = models.CharField(max_length=255, verbose_name="Registro / Matrícula")
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Usuário")
    cargo = models.ForeignKey('UserCargo', on_delete=models.CASCADE, verbose_name="Cargo")
    avatar_url = models.URLField(max_length=500, null=True, blank=True, verbose_name="URL do Avatar")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return f"Perfil de {self.user_id}"
    
    class Meta:
        verbose_name = "Perfil de Usuário"
        verbose_name_plural = "Perfis de Usuário"
    
    #get user name from user_id
    def get_user_name(self):
        return self.user_id.username
    
    #get cargo name from cargo
    def get_cargo_name(self):
        return self.cargo.name


class Client(models.Model): #Clientes
    id = models.AutoField(primary_key=True, verbose_name="ID")
    company_name = models.CharField(max_length=255, verbose_name="Razão Social")
    fantasy_name = models.CharField(max_length=255, verbose_name="Nome Fantasia")
    cpf_cnpj = models.CharField(max_length=20, unique=True, verbose_name="CPF/CNPJ")
    state_register_number = models.CharField(max_length=255, null=True, blank=True, verbose_name="Inscrição Estadual")
    email = models.EmailField(unique=True, verbose_name="Email")
    observations = models.TextField(null=True, blank=True, verbose_name="Observações")
    field_area = models.IntegerField(null=True, blank=True, verbose_name="Área de Campo (Ha)")
    address_id = models.ForeignKey('ClientAddress', on_delete=models.CASCADE, verbose_name="Endereço")
    user_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Usuário")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="Data de Modificação")

    def __str__(self):
        return str(self.fantasy_name)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"


class UserCheckIn(models.Model): #Check-ins
    id = models.AutoField(primary_key=True, verbose_name="ID")
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")
    client_id = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name="Cliente")
    seller_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Vendedor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return f"{self.latitude} - {self.longitude}"
    
    #get client name from client_id
    def get_client_name(self):
        return self.client_id.fantasy_name
    
    class Meta:
        verbose_name = "Check-In"
        verbose_name_plural = "Check-Ins"


class ClientContact(models.Model): #Contatos
    id = models.AutoField(primary_key=True, verbose_name="ID")
    client_id = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name="Cliente")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="Data de Modificação")

    def __str__(self):
        return str(self.client_id)
    
    class Meta:
        verbose_name = "Contato de Cliente"
        verbose_name_plural = "Contatos de Clientes"
    
    #get client name from client_id
    def get_client_name(self):
        return self.client_id.fantasy_name


class ClientMail(models.Model): #Emails
    id = models.AutoField(primary_key=True, verbose_name="ID")
    email = models.EmailField(unique=True, verbose_name="Email")
    responsible = models.CharField(max_length=255, verbose_name="Responsável")
    contact_id = models.ForeignKey('ClientContact', on_delete=models.CASCADE, verbose_name="Contato")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="Data de Modificação")

    def __str__(self):
        return f"E-mail: {self.email} (Responsável: {self.responsible})"
    
    class Meta:
        verbose_name = "E-mail"
        verbose_name_plural = "E-mails"


class ClientPhone(models.Model): #Telefones
    id = models.AutoField(primary_key=True, verbose_name="ID")
    phone_number = models.CharField(max_length=20, verbose_name="Número de Telefone")
    type = models.CharField(max_length=50, verbose_name="Tipo")
    responsible = models.CharField(max_length=255, verbose_name="Responsável")
    contact_id = models.ForeignKey('ClientContact', on_delete=models.CASCADE, verbose_name="Contato")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="Data de Modificação")

    def __str__(self):
        return f"Telefone: {self.phone_number}, ({self.type}) (Responsável: {self.responsible})"
    
    class Meta:
        verbose_name = "Telefone"
        verbose_name_plural = "Telefones"


class ClientAddress(models.Model): #Endereços
    id = models.AutoField(primary_key=True, verbose_name="ID")
    street = models.CharField(max_length=255, verbose_name="Rua")
    number = models.CharField(max_length=10, verbose_name="Número")
    neighborhood = models.CharField(max_length=255, verbose_name="Bairro")
    city = models.CharField(max_length=255, verbose_name="Cidade")
    cep = models.CharField(max_length=9, verbose_name="CEP")
    complement = models.CharField(max_length=255, null=True, blank=True, verbose_name="Complemento")
    state_abbreviation = models.CharField(max_length=2, verbose_name="UF")
    client_id = models.ForeignKey('Client', on_delete=models.CASCADE,  null=True, blank=True, verbose_name="Cliente")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")

    def __str__(self):
        return f"{self.street}, {self.number} - {self.neighborhood}, {self.city}, {self.state_abbreviation}"
    
    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"
    
    #get client name from client_id
    def get_client_name(self):
        return self.client_id.fantasy_name


class NegotiationStatus(models.Model): #Status da Negociação
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Nome")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Status da Negociação"
        verbose_name_plural = "Status das Negociações"


class ClientNegotiation(models.Model): #Negociações
    id = models.AutoField(primary_key=True, verbose_name="ID")
    negotiation_status = models.ForeignKey('NegotiationStatus', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Status")
    observation = models.TextField(null=True, blank=True, verbose_name="Observação")
    client_id = models.ForeignKey('Client', on_delete=models.CASCADE, verbose_name="Cliente")
    responsible_id = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name="Responsável")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="Data de Modificação")

    def __str__(self):
        return f"Negociação {self.id}, Cliente: {self.client_id}"
    
    class Meta:
        verbose_name = "Negociação"
        verbose_name_plural = "Negociações"
    
    #get client name from client_id
    def get_client_name(self):
        return self.client_id.fantasy_name


class OrderStatus(models.Model): #Status do Pedido
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Nome")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Status do Pedido"
        verbose_name_plural = "Status dos Pedidos"


class PaymentMethods(models.Model): #Formas de Pagamento
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Nome")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Forma de Pagamento"
        verbose_name_plural = "Formas de Pagamento"


class OrderShipping(models.Model): #Frete
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Nome")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Frete"
        verbose_name_plural = "Fretes"


class Order(models.Model): #Pedidos
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Nome")
    order_status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Status")
    shipping = models.ForeignKey('OrderShipping', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Frete")
    payment_method = models.ForeignKey('PaymentMethods', on_delete=models.CASCADE, null=True, blank=True, verbose_name="Forma de Pagamento")
    observation = models.TextField(null=True, blank=True, verbose_name="Observação")
    negotiation_id = models.ForeignKey('ClientNegotiation', on_delete=models.CASCADE, verbose_name="Negociação")
    payment_date = models.DateTimeField(null=True, blank=True, verbose_name="Data de Pagamento")
    payment_details = models.TextField(null=True, blank=True, verbose_name="Detalhes do Pagamento")
    cancelling_observation = models.TextField(null=True, blank=True, verbose_name="Observação de Cancelamento")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="Data de Modificação")

    def __str__(self):
        return f"Pedido {self.name}"
    
    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
    
    #get client name from negotiation_id
    def get_client_name(self):
        return self.negotiation_id.client_id.fantasy_name


class Culture(models.Model): #Culturas
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Nome")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="Data de Modificação")

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Cultura"
        verbose_name_plural = "Culturas"


class Variety(models.Model): #Variedades
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Nome")
    observation = models.TextField(null=True, blank=True, verbose_name="Observação")
    culture_id = models.ForeignKey('Culture', on_delete=models.CASCADE, verbose_name="Cultura")
    disabled_at = models.DateTimeField(null=True, blank=True, verbose_name="Data de Desativação")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="Data de Modificação")

    def __str__(self):
        return f"{self.name} - {self.culture_id.name}"
    
    class Meta:
        verbose_name = "Variedade / Cultivar"
        verbose_name_plural = "Variedades / Cultivares"
    
    #get culture name from culture_id
    def get_culture_name(self):
        return self.culture_id.name


class OrderBatch(models.Model): #Lote
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Nome")
    germination = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Germinação")
    purity = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Pureza")
    observation = models.TextField(null=True, blank=True, verbose_name="Observação")
    approved = models.BooleanField(default=False, verbose_name="Aprovado")
    variety_id = models.ForeignKey('Variety', on_delete=models.CASCADE, verbose_name="Variedade")
    quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Quantidade")
    premium = models.BooleanField(default=False, verbose_name="Premium")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="Data de Modificação")

    def __str__(self):
        return f"Lote {self.name}"
    
    class Meta:
        verbose_name = "Lote"
        verbose_name_plural = "Lotes"


class Packing(models.Model): #Embalagens
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Nome")
    unity = models.CharField(max_length=50, verbose_name="Unidade")
    volume = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Volume")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="Data de Modificação")

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Embalagem"
        verbose_name_plural = "Embalagens"


class OrderBatchPacking(models.Model): #Embalagens disponíveis para o Lote
    id = models.AutoField(primary_key=True, verbose_name="ID")
    packing_id = models.ForeignKey('Packing', on_delete=models.CASCADE, verbose_name="Embalagem")
    batch_id = models.ForeignKey('OrderBatch', on_delete=models.CASCADE, verbose_name="Lote")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")

    def __str__(self):
        return f"Embalagem {self.packing_id.name}, Lote {self.batch_id.name}"
    
    class Meta:
        verbose_name = "Embalagem por Lote"
        verbose_name_plural = "Embalagens por Lote"
    
    #get packing name from packing_id
    def get_packing_name(self):
        return self.packing_id.name
    
    #get batch name from batch_id
    def get_batch_name(self):
        return self.batch_id.name


class Tsi(models.Model): #TSI
    id = models.AutoField(primary_key=True, verbose_name="ID")
    name = models.CharField(max_length=255, verbose_name="Nome")
    receipt = models.TextField(null=True, blank=True, verbose_name="Receita")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="Data de Modificação")

    def __str__(self):
        return str(self.name)
    
    class Meta:
        verbose_name = "Tratamento de Semente"
        verbose_name_plural = "Tratamento de Sementes"


class OrderItems(models.Model): #Itens do Pedido
    id = models.AutoField(primary_key=True, verbose_name="ID")
    quantity = models.DecimalField(max_digits=65, decimal_places=30, verbose_name="Quantidade")
    unit_price = models.DecimalField(max_digits=65, decimal_places=30, verbose_name="Preço Unitário")
    description = models.TextField(null=True, blank=True, verbose_name="Descrição")
    custom_tsi = models.ForeignKey('Tsi', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="TSI Personalizado")
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name="Pedido")
    current_batch = models.ForeignKey('OrderBatch', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Lote Atual")
    packing_id = models.ForeignKey('Packing', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Embalagem")
    item_culture = models.ForeignKey('Culture', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Cultura")
    item_variety = models.ForeignKey('Variety', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Variedade")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Data de Atualização")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="Data de Modificação")

    def __str__(self):
        return f"Item {self.description}, Pedido {self.order_id}"
    
    class Meta:
        verbose_name = "Item do Pedido"
        verbose_name_plural = "Itens do Pedido"
    
    #get culture name from item_culture
    def get_culture_name(self):
        return self.item_culture.name
    
    #get variety name from item_variety
    def get_variety_name(self):
        return self.item_variety.name
    
    #get order name from order_id
    def get_order_name(self):
        return self.order_id.name
    
    #get batch name from current_batch
    def get_batch_name(self):
        return self.current_batch.name
    
    #get packing name from packing_id
    # def get_packing_name(self):
    #     return self.packing_id.name


class OrderBatchRelation(models.Model): #Relação entre Pedido e Lote
    id = models.AutoField(primary_key=True, verbose_name="ID")
    order_id = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name="Pedido")
    item_id = models.ForeignKey('OrderItems', on_delete=models.CASCADE, verbose_name="Item")
    batch_id = models.ForeignKey('OrderBatch', on_delete=models.CASCADE, verbose_name="Lote")
    requested_quantity = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Quantidade Solicitada")
    opened = models.BooleanField(default=True, verbose_name="Aberto")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="Data de Modificação")

    def __str__(self):
        return f"Pedido {self.order_id}, Lote {self.batch_id}"
    
    class Meta:
        verbose_name = "Relação Pedido / Lote"
        verbose_name_plural = "Relações Pedido / Lote"
    
    #calculate the total price of the item
    def total_price(self):
        total = self.requested_quantity * self.item_id.unit_price
        return total
    
    #get order name from order_id
    def get_order_name(self):
        return self.order_id.name
    
    #get batch name from batch_id
    def get_batch_name(self):
        return self.batch_id.name