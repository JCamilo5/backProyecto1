from django.db import models

# Create your models here.


class Enterprise(models.Model):
    """Clase Empresa"""
    name = models.CharField(max_length=45, help_text='nombre')
    historical_review = models.TextField(null=True, blank=True, help_text='reseña historica')
    location = models.CharField(max_length=45, help_text='ubicación')
    business_hours = models.CharField(max_length=45, null=True, blank=True, help_text='horario de atención')
    status = models.BooleanField(default=True, help_text='estado')
    created = models.DateTimeField(auto_now_add=True, help_text='creado') 

    def __str__(self) -> str:
        """Función que representa el objeto"""
        return self.name
