# Generated by Django 2.2.6 on 2019-12-23 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0012_auto_20191223_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='friend',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='p_library.Friend'),
        ),
    ]
