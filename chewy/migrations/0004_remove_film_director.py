# Generated by Django 2.2.3 on 2021-11-16 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chewy', '0003_auto_20190715_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='director',
        ),
    ]
