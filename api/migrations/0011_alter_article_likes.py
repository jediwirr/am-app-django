# Generated by Django 3.2.4 on 2021-06-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_article_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='likes',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
