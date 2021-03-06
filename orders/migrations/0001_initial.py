# Generated by Django 3.2 on 2021-04-25 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(help_text='cantidad')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, help_text='fecha')),
                ('status', models.BooleanField(default=True, help_text='estado')),
                ('estimated_time', models.PositiveSmallIntegerField(help_text='tiempo estimado')),
                ('location', models.CharField(help_text='ubicación', max_length=45)),
            ],
        ),
    ]
