# Generated by Django 3.0.2 on 2020-02-09 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shots', '0009_auto_20200209_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenshot',
            name='base64_full',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='screenshot',
            name='base64_thumb',
            field=models.TextField(blank=True, null=True),
        ),
    ]
