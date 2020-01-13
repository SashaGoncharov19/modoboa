# Generated by Django 1.9.12 on 2017-01-16 14:08
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relaydomains', '0002_migrate_from_modoboa_admin_relaydomains'),
    ]

    operations = [
        migrations.AddField(
            model_name='relaydomain',
            name='target_port',
            field=models.IntegerField(default=25, help_text='Remote port of this domain', verbose_name='target host port'),
        ),
        migrations.AlterField(
            model_name='relaydomain',
            name='target_host',
            field=models.CharField(help_text='Remote address (hostname or IP) of this domain', max_length=255, verbose_name='target host address'),
        ),
    ]
