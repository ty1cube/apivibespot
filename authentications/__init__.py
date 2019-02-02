from django.apps import AppConfig


class AuthenticationAppConfig(AppConfig):
    name = 'authentications'
    label = 'authentications'
    # verbose_name = 'Authentications'

    def ready(self):
        import authentications.signals

# This is how we register our custom app config with Django. Django is smart
# enough to look for the `default_app_config` property of each registered app
# and use the correct app config based on that value.
default_app_config = 'authentications.AuthenticationAppConfig'