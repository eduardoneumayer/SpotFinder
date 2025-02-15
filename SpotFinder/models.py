from django.db import models
from django.contrib.auth.models import AbstractUser


class Pessoa(AbstractUser):
    telefone = models.CharField(max_length=11, blank=True, null=True)  # Melhor usar CharField para números de telefone
    nome = models.CharField(max_length=100, blank=True, null=True)  # 'first_name' já existe no AbstractUser

    def __str__(self):
        return self.nome or self.username



class Carro(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    placa = models.CharField(max_length=10)
    codigo_venda = models.CharField(max_length=50, blank=True, null=True)
    proprietario = models.ForeignKey(
        Pessoa, on_delete=models.SET_NULL, null=True, blank=True, related_name='carros'
    )

    def __str__(self):
        return f"{self.modelo} - {self.placa}"


class Rua(models.Model):
    nome = models.CharField(max_length=100)
    num_vagas = models.PositiveIntegerField()

    def __str__(self):
        return self.nome


class Vaga(models.Model):
    localizacao = models.CharField(max_length=100)
    id_vaga = models.CharField(max_length=30)
    tamanho = models.CharField(max_length=10)
    rua = models.ForeignKey(Rua, on_delete=models.CASCADE, related_name='vagas')

    def __str__(self):
        return f"Vaga {self.id_vaga} - {self.localizacao}"


class Estacionamento(models.Model):
    carro = models.OneToOneField(Carro, on_delete=models.CASCADE, related_name='estacionamento', null=True, blank=True)
    vaga = models.OneToOneField(Vaga, on_delete=models.CASCADE, related_name='estacionamento', null=True, blank=True)
    hora = models.TimeField()
    data = models.DateField()

