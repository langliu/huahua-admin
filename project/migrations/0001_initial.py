# Generated by Django 2.0.5 on 2018-05-15 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemDetail',
            fields=[
                ('value', models.CharField(max_length=500)),
                ('list_item_id', models.IntegerField()),
                ('item_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('project_list_id', models.IntegerField()),
                ('list_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=False)),
                ('user_id', models.IntegerField()),
                ('deadline', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_name', models.CharField(max_length=200)),
                ('team_id', models.IntegerField()),
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectList',
            fields=[
                ('list_name', models.CharField(max_length=200)),
                ('project_id', models.IntegerField()),
                ('project_list_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
