# Generated by Django 3.0.5 on 2020-04-30 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_message'),
    ]

    operations = [
        migrations.DeleteModel(
            name='message',
        ),
    ]
