# Generated by Django 1.10.7 on 2017-11-24 14:06
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relaydomains', '0006_auto_20170215_0948'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipientAccess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.CharField(max_length=254, unique=True)),
                ('action', models.CharField(max_length=40)),
            ],
        ),
    ]
