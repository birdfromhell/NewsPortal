# Generated by Django 4.2 on 2023-04-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_alter_posts_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='status',
            field=models.IntegerField(choices=[(1, 'Draft'), (2, 'Published'), (3, 'Archived'), (4, 'Schedule')]),
        ),
    ]
