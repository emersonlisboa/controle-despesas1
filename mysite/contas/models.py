from django.db import models

# Create your models here.
class Conta(models.Model):
    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    pago = models.BooleanField(default=False)

    def __str__(self):
        return self.descricao