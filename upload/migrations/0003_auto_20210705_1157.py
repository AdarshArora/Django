# Generated by Django 3.2.4 on 2021-07-05 11:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='data_created',
        ),
        migrations.AddField(
            model_name='post',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
