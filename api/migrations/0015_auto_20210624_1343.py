# Generated by Django 3.2.4 on 2021-06-24 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210624_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='likes',
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
