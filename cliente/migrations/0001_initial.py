# Generated by Django 4.0.5 on 2022-06-05 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=100)),
                ('endereço_completo', models.CharField(max_length=100)),
                ('e_mail', models.CharField(max_length=100)),
                ('CPF', models.CharField(max_length=100)),
            ],
        ),
    ]