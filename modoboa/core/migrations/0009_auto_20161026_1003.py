# Generated by Django 1.9.5 on 2016-10-26 08:03
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_localconfig'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[(b'cs', '\u010de\u0161tina'), (b'de', 'deutsch'), (b'en', 'english'), (b'es', 'espa\xf1ol'), (b'fr', 'fran\xe7ais'), (b'it', 'italiano'), (b'ja_JP', '\u65e5\u672c\u306e'), (b'nl', 'nederlands'), (b'pt_PT', 'portugu\xeas'), (b'pt_BR', 'portugu\xeas (BR)'), (b'ru', '\u0440\u0443\u0441\u0441\u043a\u0438\u0439'), (b'sv', 'svenska')], default=b'en', help_text='Prefered language to display pages.', max_length=10, verbose_name='language'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='Last name'),
        ),
    ]
