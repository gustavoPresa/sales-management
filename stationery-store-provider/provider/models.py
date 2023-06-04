from decimal import Decimal

from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import DecimalField
from django.db.models import EmailField
from django.db.models import ForeignKey
from django.db.models import IntegerField
from django.db.models import Model
from django.db.models import PROTECT


class BaseUserModel(Model):
    name = CharField('Nome', max_length=50)

    email = EmailField('E-mail', max_length=100, unique=True)

    phone_number = CharField('Número de telefone', max_length=12)

    created_at = DateTimeField('Data de Criação', auto_now_add=True)

    updated_at = DateTimeField('Data de Atualização', auto_now=True)

    def __str__(self) -> str:
        return self.name


class Client(BaseUserModel):
    class Meta:
        verbose_name = 'Cliente'


class Seller(BaseUserModel):
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'


class CommissionConfig(Model):
    DAY_CHOICES = (
        ('mon', 'Segunda-feira'),
        ('tue', 'Terça-feira'),
        ('wed', 'Quarta-feira'),
        ('thu', 'Quinta-feira'),
        ('fri', 'Sexta-feira'),
        ('sat', 'Sábado'),
        ('sun', 'Domingo'),
    )

    day = CharField(
        'Dia da Semana',
        max_length=3,
        choices=DAY_CHOICES,
        unique=True
    )

    min_commission_percentage = IntegerField(
        'Mínimo de Comissão'
    )

    max_commission_percentage = IntegerField(
        'Máximo de Comissão'
    )

    def __str__(self):
        return self.get_day_display()

    class Meta:
        verbose_name = 'Configurações da Comissão'
        verbose_name_plural = 'Configurações de Comissões'


class Product(Model):
    product_code = CharField('Código do Produto', max_length=50, unique=True)

    unitary_value = DecimalField(
        'Valor Unitário',
        decimal_places=2,
        default=Decimal(0),
        max_digits=10,
    )

    description = CharField('Descrição', max_length=255)

    commission_percentage = IntegerField('Porcentagem de Comissão')

    def __str__(self) -> str:
        return self.description

    class Meta:
        verbose_name = 'Produto'


class Sale(Model):
    invoice_number = CharField(
        'Número da Nota Fiscal',
        max_length=10,
        unique=True
    )

    amount = IntegerField('Quantidade de Produtos')

    created_at = DateTimeField('Data de Criação')

    client = ForeignKey(Client, on_delete=PROTECT)

    seller = ForeignKey(Seller, on_delete=PROTECT)

    product = ForeignKey(Product, on_delete=PROTECT)

    def __str__(self) -> str:
        return self.invoice_number

    class Meta:
        verbose_name = 'Venda'
