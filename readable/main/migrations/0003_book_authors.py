# Generated by Django 3.2.4 on 2021-11-05 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211104_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.TextField(default='None'),
        ),
    ]
