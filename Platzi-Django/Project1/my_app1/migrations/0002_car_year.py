# Generated by Django 4.2.11 on 2024-07-13 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.TextField(max_length=4, null=True),
        ),
    ]
