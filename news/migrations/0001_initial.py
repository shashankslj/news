# Generated by Django 3.0.2 on 2020-03-02 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.TextField(default='', max_length='50')),
            ],
        ),
        migrations.CreateModel(
            name='News_content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('News_title', models.CharField(default='', max_length=50)),
                ('content', models.TextField(default='', max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('video', models.FileField(upload_to='')),
                ('news_category', models.TextField(default='', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.IntegerField(default='0')),
                ('Address', models.CharField(default='', max_length=100)),
                ('proffession', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('Field_location', models.TextField(default='', max_length=25)),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='News_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.TextField(default='', max_length=50)),
                ('news_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='news.News_content')),
                ('user_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
