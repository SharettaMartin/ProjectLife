# Generated by Django 3.0.8 on 2020-08-05 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20200804_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donor',
            name='birthday',
        ),
    ]