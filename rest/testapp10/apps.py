from django.apps import AppConfig


class Testapp10Config(AppConfig):
    name = 'testapp10'

    def ready(self):
        from .signals import log_user_logged_in_success