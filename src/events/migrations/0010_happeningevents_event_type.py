# Generated by Django 2.2.6 on 2019-11-19 09:33

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_remove_happeningevents_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='happeningevents',
            name='event_type',
            field=jsonfield.fields.JSONField(default=dict),
        ),
    ]
