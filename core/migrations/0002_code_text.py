# Generated by Django 3.2.25 on 2024-10-05 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='text',
            field=models.TextField(default=''),
        ),
    ]