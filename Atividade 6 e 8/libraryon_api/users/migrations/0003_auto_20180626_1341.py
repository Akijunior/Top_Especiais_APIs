# Generated by Django 2.0.3 on 2018-06-26 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180622_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='password',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lector',
            name='email',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lector',
            name='password',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
