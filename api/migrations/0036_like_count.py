# Generated by Django 3.2.4 on 2021-08-18 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_remove_like_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='count',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]