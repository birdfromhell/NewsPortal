# Generated by Django 4.2 on 2023-04-08 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0010_alter_posts_page_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
