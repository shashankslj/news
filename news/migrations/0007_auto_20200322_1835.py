# Generated by Django 3.0.2 on 2020-03-22 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news_status',
            name='news_id',
        ),
        migrations.RemoveField(
            model_name='news_status',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='News_content',
        ),
        migrations.DeleteModel(
            name='News_Status',
        ),
    ]
