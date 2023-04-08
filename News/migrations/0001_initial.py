# Generated by Django 4.2 on 2023-04-08 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='postimage/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('featured', models.BooleanField(default=False)),
                ('breaking_news', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Published'), (3, 'Archived'), (4, 'Schedule')])),
                ('page_views', models.IntegerField(default=0, editable=False)),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.author')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='News.categories')),
                ('tags', models.ManyToManyField(blank=True, to='News.tags')),
            ],
        ),
    ]
