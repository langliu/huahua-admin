# Generated by Django 2.0.5 on 2018-06-07 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20180523_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='listitem',
            name='create_time',
            field=models.DateTimeField(null=True),
        ),
    ]
