# Generated by Django 4.2.7 on 2023-11-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RealEsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(default='', max_length=100)),
                ('Description', models.CharField(default='', max_length=100)),
                ('Price', models.CharField(default='', max_length=100)),
                ('Property', models.CharField(default='', max_length=100)),
                ('Location', models.CharField(default='', max_length=100)),
                ('Bedroom', models.CharField(default='', max_length=100)),
                ('Bathrooms', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
