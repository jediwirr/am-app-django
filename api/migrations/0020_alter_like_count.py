# Generated by Django 3.2.4 on 2021-06-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20210624_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='count',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
