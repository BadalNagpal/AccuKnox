from django.apps import AppConfig

class MyAppConfig(AppConfig):
    name = 'app'

    def ready(self):
        #importing the signals module to register the signal handlers
        from . import signals