# Generated by Django 2.1.15 on 2020-05-11 20:56

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecalendar', '0007_auto_20200510_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='breedingstockevent',
            name='attributes',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='calfevent',
            name='attributes',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]