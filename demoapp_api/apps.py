from django.apps import AppConfig


class DemoappApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'demoapp_api'
    TableOfContentModel= "TableOfContentModel"
