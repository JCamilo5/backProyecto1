from django.db import models

# Create your models here.


class Client(models.Model):
    """Clase que representa un Cliente"""
    name = models.CharField(max_length=45)
    location = models.CharField(max_length=45)
    telephone = models.CharField(max_length=15)
    user = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50, default="")
    typeU = models.CharField(max_length=45, default="")
    stateU = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name
