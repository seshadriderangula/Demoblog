# Generated by Django 2.2.6 on 2019-10-31 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatha', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registerid', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.EmailField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=30),
        ),
    ]
