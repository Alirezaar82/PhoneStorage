# Generated by Django 5.1 on 2024-08-08 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=255, verbose_name='brand name')),
                ('model_name', models.CharField(max_length=255, unique=True, verbose_name='model name')),
                ('brand_nationality', models.CharField(max_length=255, verbose_name='brand nationality')),
                ('color', models.CharField(max_length=255, verbose_name='color')),
                ('screen_size', models.PositiveIntegerField(verbose_name='screen size')),
                ('status', models.IntegerField(choices=[(1, 'available'), (2, 'unavailable')], default=2, verbose_name='status')),
                ('manufacturing_country', models.CharField(max_length=255, verbose_name='manufacturing country')),
                ('price', models.PositiveIntegerField(verbose_name='price')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='datetime created')),
                ('datetime_updated', models.DateTimeField(auto_now=True, verbose_name='datetime updated')),
            ],
        ),
    ]
