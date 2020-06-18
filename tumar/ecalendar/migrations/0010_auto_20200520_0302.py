# Generated by Django 2.2.12 on 2020-05-20 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0021_auto_20200511_1929'),
        ('ecalendar', '0009_auto_20200512_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='breedingstockevent',
            name='farm',
            field=models.ForeignKey(default='efb3af89-6ddf-4dd2-b20a-84a28bf55a45', on_delete=django.db.models.deletion.CASCADE, to='animals.Farm', verbose_name='Farm'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='calfevent',
            name='farm',
            field=models.ForeignKey(default='efb3af89-6ddf-4dd2-b20a-84a28bf55a45', on_delete=django.db.models.deletion.CASCADE, to='animals.Farm', verbose_name='Farm'),
            preserve_default=False,
        ),
    ]