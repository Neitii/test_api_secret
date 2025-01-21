from django.contrib import admin


from .models import Secret

@admin.register(Secret)
class TagAdmin(admin.ModelAdmin):
    """Настройка панели администрирования модели секретов."""

    list_display = ("passphrase", "secret","secret_key")
    search_fields = ("secret_key",)
    list_filter = ("secret_key",)
    empty_value_display = "(не задано)"
