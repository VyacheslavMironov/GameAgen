# Generated by Django 4.0.1 on 2022-05-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
    ]