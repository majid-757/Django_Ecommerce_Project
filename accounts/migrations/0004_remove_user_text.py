# Generated by Django 3.0 on 2022-09-12 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='text',
        ),
    ]
