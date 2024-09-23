# Generated by Django 5.1.1 on 2024-09-23 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_perfil'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='biografia',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='apellido',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
