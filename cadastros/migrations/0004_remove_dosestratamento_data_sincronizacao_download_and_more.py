# Generated by Django 4.0.4 on 2022-09-05 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_dosestratamento_status_tratamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosestratamento',
            name='data_sincronizacao_download',
        ),
        migrations.RemoveField(
            model_name='dosestratamento',
            name='data_sincronizacao_upload',
        ),
        migrations.RemoveField(
            model_name='dosestratamento',
            name='status_sincronizacao_download',
        ),
        migrations.RemoveField(
            model_name='dosestratamento',
            name='status_sincronização_upload',
        ),
    ]
