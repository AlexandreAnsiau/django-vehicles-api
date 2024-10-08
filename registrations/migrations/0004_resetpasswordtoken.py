# Generated by Django 5.1.1 on 2024-09-12 15:01

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0003_remove_customuser_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetPasswordToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='clé')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")),
                ('is_used', models.BooleanField(default=False, verbose_name='est utilisé')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='utilisateur')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
