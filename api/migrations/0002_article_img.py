# Generated by Django 3.2.3 on 2021-05-31 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.ImageField(height_field=100, null=True, upload_to='../APIproject/images', width_field=100),
        ),
    ]