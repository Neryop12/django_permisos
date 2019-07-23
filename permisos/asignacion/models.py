# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from asignacion.modelMFCGT import DMarca



class Accounts(models.Model):
    accountsid = models.CharField(db_column='AccountsID', primary_key=True, max_length=200)  # Field name made lowercase.
    account = models.CharField(db_column='Account', max_length=200, blank=True, null=True)  # Field name made lowercase.
    media = models.CharField(db_column='Media', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts'
    def __str__(self):
        return '{} - {}'.format(self.account, self.media)
        

   


class Ads(models.Model):
    adid = models.CharField(db_column='AdID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    adname = models.CharField(db_column='Adname', max_length=200, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=200, blank=True, null=True)  # Field name made lowercase.
    adstatus = models.CharField(db_column='Adstatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    adsetid = models.CharField(db_column='AdSetID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ads'


class Adsetmetrics(models.Model):
    reach = models.IntegerField(db_column='Reach', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=45, blank=True, null=True)  # Field name made lowercase.
    adsetname = models.CharField(db_column='AdSetname', max_length=45, blank=True, null=True)  # Field name made lowercase.
    adsetid = models.CharField(db_column='AdSetID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.
    impressions = models.IntegerField(db_column='Impressions', blank=True, null=True)  # Field name made lowercase.
    clicks = models.CharField(db_column='Clicks', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adsetmetrics'


class Adsets(models.Model):
    adsetid = models.CharField(db_column='AdSetID', primary_key=True, max_length=45)  # Field name made lowercase.
    adsetname = models.CharField(db_column='Adsetname', max_length=200, blank=True, null=True)  # Field name made lowercase.
    adsetlifetimebudget = models.FloatField(db_column='Adsetlifetimebudget', blank=True, null=True)  # Field name made lowercase.
    adsetdailybudget = models.FloatField(db_column='Adsetdailybudget', blank=True, null=True)  # Field name made lowercase.
    adsettargeting = models.TextField(db_column='Adsettargeting', blank=True, null=True)  # Field name made lowercase.
    adsetend = models.DateField(db_column='Adsetend', blank=True, null=True)  # Field name made lowercase.
    adsetstart = models.DateField(db_column='Adsetstart', blank=True, null=True)  # Field name made lowercase.
    typeadset = models.IntegerField(db_column='TypeAdSet', blank=True, null=True)  # Field name made lowercase.
    campaingid = models.CharField(db_column='CampaingID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adsets'


class Campaingdisplay(models.Model):
    publisherplatform = models.CharField(db_column='Publisherplatform', max_length=45, blank=True, null=True)  # Field name made lowercase.
    placement = models.CharField(db_column='Placement', max_length=200, blank=True, null=True)  # Field name made lowercase.
    campaingid = models.CharField(db_column='CampaingID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'campaingdisplay'


class Campaingmetrics(models.Model):
    reach = models.IntegerField(db_column='Reach', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    clicks = models.IntegerField(db_column='Clicks', blank=True, null=True)  # Field name made lowercase.
    percentofbudgetused = models.FloatField(db_column='Percentofbudgetused', blank=True, null=True)  # Field name made lowercase.
    impressions = models.IntegerField(db_column='Impressions', blank=True, null=True)  # Field name made lowercase.
    placement = models.CharField(db_column='Placement', max_length=45, blank=True, null=True)  # Field name made lowercase.
    campaingid = models.CharField(db_column='CampaingID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'campaingmetrics'


class Campaings(models.Model):
    campaingid = models.CharField(db_column='CampaingID', primary_key=True, max_length=45)  # Field name made lowercase.
    campaingname = models.CharField(db_column='Campaingname', max_length=200, blank=True, null=True)  # Field name made lowercase.
    campaignspendinglimit = models.FloatField(db_column='Campaignspendinglimit', blank=True, null=True)  # Field name made lowercase.
    campaigndailybudget = models.FloatField(db_column='Campaigndailybudget', blank=True, null=True)  # Field name made lowercase.
    campaignlifetimebudget = models.FloatField(db_column='Campaignlifetimebudget', blank=True, null=True)  # Field name made lowercase.
    campaignobjective = models.CharField(db_column='Campaignobjective', max_length=200, blank=True, null=True)  # Field name made lowercase.
    campaignstatus = models.CharField(db_column='Campaignstatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    accountsid = models.CharField(db_column='AccountsID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'campaings'


class Creativeads(models.Model):
    adcreativeid = models.CharField(db_column='AdcreativeID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    creativename = models.CharField(db_column='Creativename', max_length=200, blank=True, null=True)  # Field name made lowercase.
    linktopromotedpost = models.CharField(db_column='Linktopromotedpost', max_length=500, blank=True, null=True)  # Field name made lowercase.
    adcreativethumbnailurl = models.CharField(db_column='AdcreativethumbnailURL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    adcreativeimageurl = models.CharField(db_column='AdcreativeimageURL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    externaldestinationurl = models.CharField(db_column='ExternaldestinationURL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    adcreativeobjecttype = models.CharField(db_column='Adcreativeobjecttype', max_length=200, blank=True, null=True)  # Field name made lowercase.
    promotedpostid = models.IntegerField(db_column='PromotedpostID', blank=True, null=True)  # Field name made lowercase.
    promotedpostname = models.CharField(db_column='Promotedpostname', max_length=200, blank=True, null=True)  # Field name made lowercase.
    promotedpostinstagramid = models.IntegerField(db_column='PromotedpostInstagramID', blank=True, null=True)  # Field name made lowercase.
    promotedpostmessage = models.CharField(db_column='Promotedpostmessage', max_length=200, blank=True, null=True)  # Field name made lowercase.
    promotedpostcaption = models.CharField(db_column='Promotedpostcaption', max_length=500, blank=True, null=True)  # Field name made lowercase.
    promotedpostdestinationurl = models.CharField(db_column='PromotedpostdestinationURL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    promotedpostimageurl = models.CharField(db_column='PromotedpostimageURL', max_length=500, blank=True, null=True)  # Field name made lowercase.
    linktopromotedinstagrampost = models.CharField(db_column='LinktopromotedInstagrampost', max_length=200, blank=True, null=True)  # Field name made lowercase.
    adid = models.CharField(db_column='AdID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    adname = models.CharField(db_column='Adname', max_length=200, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(max_length=200, blank=True, null=True)
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'creativeads'


class Errorscampaings(models.Model):
    iderrorscampaings = models.AutoField(db_column='idErrorsCampaings', primary_key=True)  # Field name made lowercase.
    error = models.CharField(db_column='Error', max_length=500, blank=True, null=True)  # Field name made lowercase.
    comentario = models.CharField(db_column='Comentario', max_length=500, blank=True, null=True)  # Field name made lowercase.
    estado = models.IntegerField(db_column='Estado', blank=True, null=True)  # Field name made lowercase.
    media = models.CharField(db_column='Media', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tipoerrorid = models.IntegerField(db_column='TipoErrorID', blank=True, null=True)  # Field name made lowercase.
    campaingid = models.CharField(db_column='CampaingID', max_length=200, blank=True, null=True)  # Field name made lowercase.
    usuariovalidacion = models.IntegerField(db_column='UsuarioValidacion', blank=True, null=True)  # Field name made lowercase.
    impressions = models.IntegerField(db_column='Impressions', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'errorscampaings'


class Marcaaccount(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    idmarca = models.ForeignKey(DMarca, models.DO_NOTHING,  db_column='idmarca', blank=True, null=True)  # Field name made lowercase.
    idaccountsid = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='idaccountsid')
    usrcreation = models.IntegerField(db_column='usrcreation', blank=True, null=True)  # Field name made lowercase.
    datecreation = models.DateTimeField()
    usrmod = models.IntegerField(db_column='usrmod', blank=True, null=True)  # Field name made lowercase.
    datemod = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
        managed = False
        db_table = "marcaaccount"
        app_label = 'marca'


class Metricsads(models.Model):
    impressions = models.IntegerField(db_column='Impressions', blank=True, null=True)  # Field name made lowercase.
    ctr = models.FloatField(db_column='Ctr', blank=True, null=True)  # Field name made lowercase.
    cpm = models.FloatField(db_column='Cpm', blank=True, null=True)  # Field name made lowercase.
    cro = models.FloatField(db_column='Cro', blank=True, null=True)  # Field name made lowercase.
    cost = models.FloatField(db_column='Cost', blank=True, null=True)  # Field name made lowercase.
    frequency = models.FloatField(db_column='Frequency', blank=True, null=True)  # Field name made lowercase.
    reach = models.IntegerField(db_column='Reach', blank=True, null=True)  # Field name made lowercase.
    pagelikes = models.IntegerField(db_column='Pagelikes', blank=True, null=True)  # Field name made lowercase.
    peopletakingaction = models.IntegerField(db_column='Peopletakingaction', blank=True, null=True)  # Field name made lowercase.
    postreactions = models.IntegerField(db_column='Postreactions', blank=True, null=True)  # Field name made lowercase.
    postshares = models.IntegerField(db_column='Postshares', blank=True, null=True)  # Field name made lowercase.
    photoviews = models.IntegerField(db_column='Photoviews', blank=True, null=True)  # Field name made lowercase.
    clickstoplayvideo = models.IntegerField(db_column='Clickstoplayvideo', blank=True, null=True)  # Field name made lowercase.
    outboundclicks = models.IntegerField(db_column='Outboundclicks', blank=True, null=True)  # Field name made lowercase.
    leads = models.IntegerField(db_column='Leads', blank=True, null=True)  # Field name made lowercase.
    convertions = models.IntegerField(db_column='Convertions', blank=True, null=True)  # Field name made lowercase.
    eventresponses = models.IntegerField(db_column='Eventresponses', blank=True, null=True)  # Field name made lowercase.
    messagingreplies = models.IntegerField(db_column='Messagingreplies', blank=True, null=True)  # Field name made lowercase.
    videowatchesat75 = models.IntegerField(db_column='Videowatchesat75', blank=True, null=True)  # Field name made lowercase.
    videowatchesat100 = models.IntegerField(db_column='Videowatchesat100', blank=True, null=True)  # Field name made lowercase.
    websiteleads = models.IntegerField(db_column='Websiteleads', blank=True, null=True)  # Field name made lowercase.
    desktopappinstalls = models.IntegerField(db_column='Desktopappinstalls', blank=True, null=True)  # Field name made lowercase.
    mobileappinstalls = models.IntegerField(db_column='Mobileappinstalls', blank=True, null=True)  # Field name made lowercase.
    adid = models.CharField(db_column='AdID', max_length=45, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=45, blank=True, null=True)  # Field name made lowercase.
    adname = models.CharField(db_column='Adname', max_length=200, blank=True, null=True)  # Field name made lowercase.
    clicks = models.IntegerField(db_column='Clicks', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'metricsads'


class Platformsclientes(models.Model):
    platformclienteid = models.IntegerField(db_column='PlatformClienteID', primary_key=True)  # Field name made lowercase.
    clienteid = models.IntegerField(db_column='ClienteID', blank=True, null=True)  # Field name made lowercase.
    accountsid = models.IntegerField(db_column='AccountsID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'platformsclientes'


class Tiposerrores(models.Model):
    tipoerrorid = models.AutoField(db_column='TipoErrorID', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=100, blank=True, null=True)  # Field name made lowercase.
    icono = models.CharField(db_column='Icono', max_length=45, blank=True, null=True)  # Field name made lowercase.
    tipousuario = models.IntegerField(db_column='TipoUsuario', blank=True, null=True)  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='CreateDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tiposerrores'


class Usercuenta(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    iduser = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='iduser')
    idaccount = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='idaccount')
    usrcreation = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usrcreation')
    datecreation = models.DateTimeField()
    usrmod = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='usrmod', blank=True, null=True)
    datemod = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        abstract = True
        db_table = 'usercuenta'


