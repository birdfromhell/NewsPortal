# Generated by Django 4.2 on 2023-04-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0007_alter_posts_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='page_views',
            field=models.IntegerField(default=0),
        ),
    ]
