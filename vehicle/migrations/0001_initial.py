# Generated by Django 3.2.9 on 2021-12-08 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('driver', '0005_alter_driver_update_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=250)),
                ('model', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('plate_number', models.CharField(max_length=250)),
                ('driver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='driver.driver')),
            ],
        ),
    ]
