from django.db import models


class Secret(models.Model):
    """Модель ингредиентов рецепта."""

    secret = models.TextField(
        verbose_name="Секрет"
    )
    passphrase = models.TextField(
        verbose_name="Кодовая фраза"
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата и время публикации",
        auto_now_add=True
    )
    secret_key = models.TextField(
        verbose_name="Ссылка"
    )

    class Meta:
        """Конфигурация модели ингредиентов рецепта."""

        verbose_name = "Секрет"
        verbose_name_plural = "Секреты"
        ordering = ("-pub_date",)

    def __str__(self):
        return self.secret_key
