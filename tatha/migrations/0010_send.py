# Generated by Django 2.2.6 on 2019-11-05 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatha', '0009_register_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]