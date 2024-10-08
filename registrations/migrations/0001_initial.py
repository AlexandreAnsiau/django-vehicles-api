# Generated by Django 5.0.6 on 2024-09-05 20:34

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='créé à')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='modifié à')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=500, unique=True)),
                ('is_active', models.BooleanField(blank=True, default=True)),
                ('is_staff', models.BooleanField(blank=True, default=False)),
                ('is_superuser', models.BooleanField(blank=True, default=False)),
                ('is_visible', models.BooleanField(blank=True, default=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='prénom')),
                ('last_name', models.CharField(max_length=100, verbose_name='nom de famille')),
                ('slug', models.SlugField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='companies.company', verbose_name='entreprise')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'utilisateur',
                'verbose_name_plural': 'utilisateurs',
            },
        ),
    ]
