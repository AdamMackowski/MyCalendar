# Generated by Django 3.1.5 on 2021-05-14 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycalendar', '0007_report_bugs'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pal',
            field=models.TextField(default='blue'),
        ),
    ]
