# Generated by Django 2.1 on 2018-08-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20180818_2325'),
        ('users', '0004_auto_20180630_0359'),
    ]

    operations = [
        migrations.AddField(
            model_name='lector',
            name='favorite_books',
            field=models.ManyToManyField(to='books.Book'),
        ),
    ]
