# Generated by Django 3.1.6 on 2021-02-18 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0004_auto_20210218_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='upload',
            field=models.FileField(upload_to='drinks/uploads/'),
        ),
    ]
