# Generated by Django 4.0.4 on 2022-09-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0006_dosestratamento_horario_dose'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosestratamento',
            name='compartimento',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
