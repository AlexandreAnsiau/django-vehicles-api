# Generated by Django 5.0.6 on 2024-09-09 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Entreprise', 'verbose_name_plural': 'Entreprises'},
        ),
    ]
