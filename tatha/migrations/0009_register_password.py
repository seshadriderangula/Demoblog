# Generated by Django 2.2.6 on 2019-11-05 04:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tatha', '0008_auto_20191104_0820'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
    ]