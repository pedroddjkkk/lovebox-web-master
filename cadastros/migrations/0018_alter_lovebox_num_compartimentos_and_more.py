# Generated by Django 4.0.4 on 2022-08-22 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0017_alter_lovebox_parceiro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lovebox',
            name='num_compartimentos',
            field=models.CharField(max_length=500, verbose_name='Número de Compartimentos'),
        ),
        migrations.AlterField(
            model_name='lovebox',
            name='proprietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.paciente', verbose_name='Proprietário'),
        ),
        migrations.AlterField(
            model_name='lovebox',
            name='tempo_alerta_geral',
            field=models.IntegerField(verbose_name='Tempo de Alerta Geral(min)'),
        ),
        migrations.AlterField(
            model_name='tratamento',
            name='concetracao',
            field=models.FloatField(verbose_name='Concentração'),
        ),
        migrations.AlterField(
            model_name='tratamento',
            name='data_prescricao',
            field=models.DateField(verbose_name='Data da Prescrição'),
        ),
    ]