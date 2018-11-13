from django.db import models

class Solicitud (models.Model):
    id =models.AutoField(primary_key=True)
    correo =models.CharField(max_length=100)
    tipo =models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    voucher = models.FileField(upload_to='storage/images/', max_length=250, null=True)

    class Meta:
        db_table = "solicitudes"
    
    def __str__(self):
        return self.tipo 
