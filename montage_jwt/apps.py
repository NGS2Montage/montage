from django.apps import AppConfig

class MontageJwtConfig(AppConfig):
    name = 'montage_jwt'

    def ready(self):
        from . import signals
