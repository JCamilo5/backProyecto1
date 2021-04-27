# Generated by Django 3.2 on 2021-04-25 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('profiles.userprofile',),
        ),
        migrations.CreateModel(
            name='Courier',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('profiles.userprofile',),
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('profiles.userprofile',),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(help_text='nombres', max_length=45)),
                ('lastnames', models.CharField(help_text='apellidos', max_length=45)),
                ('location', models.CharField(help_text='ubicación', max_length=45)),
                ('telephone', models.CharField(help_text='telefono', max_length=15)),
                ('license_plate', models.CharField(blank=True, help_text='placa', max_length=6, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='creado')),
                ('updated', models.DateTimeField(auto_now=True, help_text='actualizado')),
                ('user', models.ForeignKey(help_text='usuario', on_delete=django.db.models.deletion.CASCADE, related_name='contact', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]