# Generated by Django 2.2.6 on 2019-11-04 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatha', '0005_auto_20191104_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='register',
            name='zip',
            field=models.IntegerField(max_length=30),
        ),
    ]
