from rest_framework import serializers

from .models import Secret


class GenerateSerializer(serializers.ModelSerializer):
    """secret: сериализатор создания записи."""

    class Meta:

        model = Secret
        exclude = ("pub_date", "secret_key")


class SecretSerializer(serializers.ModelSerializer):
    """secret: сериализатор выдачи."""

    def validate(self, data):
        """Валидация фразы и кода."""
        passphrase = data.get('passphrase')
        secret_key = self.context.get('secret_key')  
        try:
            secret = Secret.objects.get(passphrase=passphrase,
                                        secret_key=secret_key)
        except Secret.DoesNotExist:
            raise serializers.ValidationError('Не верно')
        data['secret'] = secret.secret
        return data

    class Meta:

        model = Secret
        fields = ("passphrase",)
