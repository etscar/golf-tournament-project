# Generated by Django 3.1.7 on 2021-04-08 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0002_golfer_managed_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='golfer',
            name='golfer_city',
            field=models.TextField(blank=True, default='unknown'),
        ),
    ]
