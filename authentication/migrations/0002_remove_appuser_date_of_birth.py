# Generated by Django 4.1.6 on 2023-02-14 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='date_of_birth',
        ),
    ]