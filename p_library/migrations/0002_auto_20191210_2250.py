# Generated by Django 2.2.6 on 2019-12-10 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='copy_count',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
