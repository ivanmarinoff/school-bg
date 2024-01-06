from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "school_bg.users"

    def ready(self):
        import school_bg.users.signals
        result = super().ready()
        return result
