from django.apps import AppConfig


class BaseInfoAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base_info_app'
