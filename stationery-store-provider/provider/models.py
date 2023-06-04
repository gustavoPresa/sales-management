from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import EmailField
from django.db.models import Model


class BaseUserModel(Model):
    name = CharField('Nome', max_length=50)

    email = EmailField('E-mail', max_length=100, unique=True)

    phone_number = CharField('Número de telefone', max_length=12)

    created_at = DateTimeField('Data de Criação', auto_now_add=True)

    updated_at = DateTimeField('Data de Atualização', auto_now=True)

    def __str__(self) -> str:
        return self.email


class Client(BaseUserModel):
    class Meta:
        verbose_name = 'Cliente'


class Seller(BaseUserModel):
    class Meta:
        verbose_name = 'Vendedor'
        verbose_name_plural = 'Vendedores'
