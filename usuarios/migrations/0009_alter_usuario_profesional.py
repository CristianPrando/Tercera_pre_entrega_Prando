# Generated by Django 5.1.1 on 2024-09-25 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_perfil_matricula_usuario_profesional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='profesional',
            field=models.BooleanField(null=True),
        ),
    ]
