# Generated by Django 2.2.6 on 2019-11-19 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20191119_0753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='happeningevents',
            name='type',
        ),
    ]
