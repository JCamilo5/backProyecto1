# Generated by Django 3.2 on 2021-04-25 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('enterprises', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='management',
            name='manager',
            field=models.ForeignKey(help_text='administrador del establecimiento', on_delete=django.db.models.deletion.CASCADE, related_name='managements', to='users.manager'),
        ),
        migrations.AddField(
            model_name='enterprise',
            name='image',
            field=models.OneToOneField(blank=True, help_text='imagen', null=True, on_delete=django.db.models.deletion.CASCADE, to='products.image'),
        ),
        migrations.AddField(
            model_name='enterprise',
            name='managers',
            field=models.ManyToManyField(help_text='administradores de establecimiento', related_name='enterprises', through='enterprises.Management', to='users.Manager'),
        ),
    ]
