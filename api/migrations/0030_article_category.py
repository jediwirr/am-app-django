# Generated by Django 3.2.4 on 2021-08-09 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0029_alter_like_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
