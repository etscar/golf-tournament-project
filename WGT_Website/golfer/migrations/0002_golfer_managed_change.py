# Generated by Django 3.1.7 on 2021-04-08 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('golfer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='golfer',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='golferroundscores',
            options={'managed': False, 'verbose_name': 'Golfer Round Score', 'verbose_name_plural': 'Golfer Round Scores'},
        ),
        migrations.AlterModelOptions(
            name='tourngolfer',
            options={'managed': False, 'verbose_name': 'Tournament Golfer', 'verbose_name_plural': 'Tournament Golfers'},
        ),
    ]
