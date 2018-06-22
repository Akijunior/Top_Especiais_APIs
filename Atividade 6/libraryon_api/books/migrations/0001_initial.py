# Generated by Django 2.0.3 on 2018-06-22 19:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('description', models.CharField(max_length=400)),
                ('isbn', models.CharField(max_length=20)),
                ('edition', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('amount_pages', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('age_range', models.CharField(choices=[('F', 'Free'), ('FT', '+14'), ('ST', '+16'), ('ET', '+18')], default='F', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.DecimalField(decimal_places=2, max_digits=4, validators=[django.core.validators.MaxValueValidator(10.0), django.core.validators.MinValueValidator(0.0)])),
                ('comment', models.CharField(blank=True, max_length=200)),
                ('evaluation_date', models.DateTimeField(auto_now_add=True)),
                ('last_update_date', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
            ],
        ),
    ]
