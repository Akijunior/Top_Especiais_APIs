# Generated by Django 2.0.3 on 2018-06-23 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20180622_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='lector',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
