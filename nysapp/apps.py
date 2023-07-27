from django.apps import AppConfig


class NysappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'nysapp'

    def ready(self):
        # import signal handlers
        import nysapp.signals

