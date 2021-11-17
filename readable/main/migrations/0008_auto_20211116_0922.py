# Generated by Django 3.2.4 on 2021-11-16 08:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0007_alter_readingprogress_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='readingprogress',
            name='id',
        ),
        migrations.AlterField(
            model_name='readingprogress',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]