# Generated by Django 3.2.13 on 2022-06-16 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rastreio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereço', models.CharField(max_length=100)),
                ('remetente', models.CharField(max_length=100)),
                ('codigo_de_rastreio', models.CharField(max_length=100)),
            ],
        ),
    ]