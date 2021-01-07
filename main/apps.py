from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    # Add this to use signals
    def ready(self):
        from . import signals