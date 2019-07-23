# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Usuario(models.Model):
    idusuario = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    clave = models.CharField(max_length=255, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)
    rol = models.IntegerField(blank=True, null=True)
    fechacrea = models.DateTimeField(blank=True, null=True)
    ultimolog = models.DateTimeField(blank=True, null=True)
    autcam = models.IntegerField(blank=True, null=True)
    rdigital = models.IntegerField(blank=True, null=True)
    rplat1 = models.IntegerField(blank=True, null=True)
    rplat2 = models.IntegerField(blank=True, null=True)
    rplat3 = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    idasignadoa = models.IntegerField(blank=True, null=True)
    rutaimagen = models.CharField(max_length=200, blank=True, null=True)
    pinpublico = models.IntegerField(blank=True, null=True)
    rolu = models.IntegerField(blank=True, null=True)
    puesto = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'
        app_label = 'user'
