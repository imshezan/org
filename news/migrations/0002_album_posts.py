# Generated by Django 2.0 on 2018-03-28 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=9000)),
                ('category', models.CharField(max_length=100)),
                ('is_favorite', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disc_title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=9000)),
                ('video_file', models.FileField(default='', upload_to='')),
                ('picture', models.FileField(upload_to='')),
                ('is_favorite', models.BooleanField(default=False)),
                ('disc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Album')),
            ],
        ),
    ]
