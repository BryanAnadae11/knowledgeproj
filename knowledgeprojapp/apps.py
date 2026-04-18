from django.apps import AppConfig


class KnowledgeprojappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'knowledgeprojapp'

    def ready(self):
    	import knowledgeprojapp.signals
