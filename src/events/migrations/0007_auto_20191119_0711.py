# Generated by Django 2.2.6 on 2019-11-19 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='happeningevents',
            name='type',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='prime_interest',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
