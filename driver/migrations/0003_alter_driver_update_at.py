# Generated by Django 3.2.9 on 2021-12-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0002_alter_driver_update_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='update_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]