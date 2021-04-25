# Generated by Django 3.2 on 2021-04-25 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprises', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='nombre', max_length=45)),
                ('price', models.PositiveBigIntegerField(help_text='precio')),
                ('ingredients', models.TextField(help_text='ingredientes')),
                ('preparation', models.TextField(blank=True, help_text='preparación', null=True)),
                ('estimated_time', models.PositiveSmallIntegerField(help_text='tiempo estimado')),
                ('accompaniments', models.ManyToManyField(blank=True, help_text='acompañamientos', related_name='_products_product_accompaniments_+', to='products.Product')),
                ('enterprise', models.ForeignKey(help_text='establecimiento', on_delete=django.db.models.deletion.CASCADE, related_name='products', to='enterprises.enterprise')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to='uploads/images')),
                ('product', models.ForeignKey(help_text='producto', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
        ),
    ]
