# Generated by Django 2.1 on 2018-08-19 02:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20180622_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='score_average',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, validators=[django.core.validators.MaxValueValidator(10.0), django.core.validators.MinValueValidator(0.0)]),
        ),
        migrations.AddField(
            model_name='book',
            name='thumb',
            field=models.ImageField(blank=True, default='book.png', null=True, upload_to='core/images', verbose_name='Imagem representativa'),
        ),
    ]
