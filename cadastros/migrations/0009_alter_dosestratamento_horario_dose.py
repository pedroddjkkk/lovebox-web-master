# Generated by Django 4.1.2 on 2023-03-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0008_dosestratamento_um'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosestratamento',
            name='horario_dose',
            field=models.TimeField(blank=True, null=True),
        ),
    ]