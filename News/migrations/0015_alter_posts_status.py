# Generated by Django 4.2 on 2023-04-09 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0014_remove_posts_breaking_news_posts_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived'), ('schedule', 'Schedule')], max_length=20),
        ),
    ]
