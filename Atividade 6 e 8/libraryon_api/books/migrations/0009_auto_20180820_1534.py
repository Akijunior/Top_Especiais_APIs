# Generated by Django 2.1 on 2018-08-20 18:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20180818_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='lector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scores', to=settings.AUTH_USER_MODEL),
        ),
    ]