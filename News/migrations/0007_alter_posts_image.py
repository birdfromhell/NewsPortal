# Generated by Django 4.2 on 2023-04-07 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0006_alter_posts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, upload_to='postimage/'),
        ),
    ]
