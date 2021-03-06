# Generated by Django 3.2.9 on 2021-11-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('rooms', models.CharField(max_length=100)),
                ('baths', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='House')),
            ],
            options={
                'verbose_name': 'House',
                'verbose_name_plural': 'Houses',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
