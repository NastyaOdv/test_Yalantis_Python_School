# Generated by Django 3.2.9 on 2021-12-07 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_alter_driver_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]