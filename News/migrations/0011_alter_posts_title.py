# Generated by Django 4.2 on 2023-04-09 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0010_site_favicon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
