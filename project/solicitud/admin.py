from django.contrib import admin

from .models import Solicitud


class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('id','correo','tipo','motivo','voucher')
    
admin.site.register(Solicitud, SolicitudAdmin)