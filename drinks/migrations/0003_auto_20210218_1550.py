# Generated by Django 3.1.6 on 2021-02-18 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0002_drink_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='upload',
            field=models.FileField(upload_to='drinks/static/uploads/'),
        ),
    ]
