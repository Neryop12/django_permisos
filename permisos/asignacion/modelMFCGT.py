# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class DMarca(models.Model):
    id = models.IntegerField(db_column='id', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='nombre', max_length=200, blank=True, null=True)  # Field name made lowercase.
    abreviatura = models.CharField(db_column='abreviatura', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idcliente = models.IntegerField(db_column='idcliente')  # Field name made lowercase.
    usering = models.IntegerField(db_column='usering')  # Field name made lowercase.
    fechaing = models.DateTimeField(db_column='fechaing')  # Field name made lowercase.
    usermod = models.IntegerField(db_column='usermod')  # Field name made lowercase.
    fechamod = models.DateTimeField(db_column='fechamod')  # Field name made lowercase.
    estado = models.IntegerField(db_column='estado')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'dmarca'
        app_label = 'mfcgt'
    def __str__(self):
        return '{}'.format(self.nombre)
        
        