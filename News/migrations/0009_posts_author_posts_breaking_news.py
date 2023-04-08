# Generated by Django 4.2 on 2023-04-07 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('News', '0008_posts_page_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.ManyToManyField(blank=True, to='users.author'),
        ),
        migrations.AddField(
            model_name='posts',
            name='breaking_news',
            field=models.BooleanField(default=False),
        ),
    ]