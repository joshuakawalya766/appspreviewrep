# Generated by Django 3.2.7 on 2021-11-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0002_auto_20211125_0655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='profile',
            field=models.ImageField(default='default.jpg', upload_to='ProfilePics/'),
        ),
    ]
