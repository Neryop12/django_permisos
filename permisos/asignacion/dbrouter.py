#Clase para enrutar la base de datos a la cual se quiere leer o escribir datos
#Toma los esquemas de el archivo settings.py DATABASES


class DatabaseForDevOps(object):
    #Seleccionar el esquema para leer datos
    def db_for_read(self, model, **hints):
        #se pregunta por las app_label colocadas en los modelos
        if model._meta.app_label in ['mfcgt']:
            return 'mfcgt'
        # Returning None is no opinion, defer to other routers or default database
        else :
            if model._meta.app_label in ['user']: 
                return 'omgguate'
        #La base de datos default es Mediaplatforms
        return 'default'
    def db_for_write(self, model, **hints):
        if model._meta.app_label in [ 'marca', 'admin','sessions','contenttypes']:
            return 'mfcgt'
         # Returning None is no opinion, defer to other routers or default database
        return 'default'
   
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'default':
            # Migrate Django core app models if current database is devops
            if app_label in ['mfcgt','user']:
                return False            
            else:
                # Non Django core app models should not be migrated if database is devops
                return True
        # Other database should not migrate Django core app models            
      