# Generated by Django 4.2.1 on 2023-06-02 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timezone',
            name='timezone_str',
        ),
    ]