# Generated by Django 3.2.4 on 2021-06-28 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hack', '0006_auto_20210622_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='checkDate',
            field=models.DateField(default='2021-01-01'),
        ),
    ]
