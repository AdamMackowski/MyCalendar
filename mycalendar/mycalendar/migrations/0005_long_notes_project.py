# Generated by Django 3.1.5 on 2021-05-11 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mycalendar', '0004_auto_20210507_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='Long_notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('notes', models.ManyToManyField(blank=True, related_name='project_notes', to='mycalendar.Long_notes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='long_User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
