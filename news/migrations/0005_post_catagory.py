# Generated by Django 2.0 on 2018-04-05 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20180406_0510'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='catagory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='news.Category'),
        ),
    ]
