# Generated by Django 2.2.6 on 2020-01-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0014_auto_20191223_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]