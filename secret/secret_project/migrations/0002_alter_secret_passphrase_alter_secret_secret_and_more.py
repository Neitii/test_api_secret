# Generated by Django 5.1.3 on 2025-01-12 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secret_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secret',
            name='passphrase',
            field=models.TextField(max_length=254, verbose_name='Кодовая фраза'),
        ),
        migrations.AlterField(
            model_name='secret',
            name='secret',
            field=models.TextField(max_length=254, verbose_name='Секрет'),
        ),
        migrations.AlterField(
            model_name='secret',
            name='secret_key',
            field=models.TextField(max_length=254, verbose_name='Ссылка'),
        ),
    ]
