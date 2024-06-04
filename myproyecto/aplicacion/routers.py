class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'secondary_app':
            return 'secondary'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._state.db in ('default', 'secondary') and obj2._state.db in ('default', 'secondary'):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'secondary_app':
            return db == 'secondary'
        return db == 'default'