# Generated by Django 2.1.5 on 2019-02-26 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songlist',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='songlist',
            name='song',
            field=models.FileField(blank=True, null=True, upload_to='track/'),
        ),
    ]