# Generated by Django 4.1 on 2022-09-23 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elefante', '0006_alter_dados_cadastro_senha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_cadastro',
            name='senha',
            field=models.IntegerField(max_length=20),
        ),
    ]
