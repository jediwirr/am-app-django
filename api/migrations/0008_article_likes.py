# Generated by Django 3.2.4 on 2021-06-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='likes',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
