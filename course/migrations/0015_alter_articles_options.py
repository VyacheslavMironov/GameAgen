# Generated by Django 4.0.1 on 2022-05-18 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0014_alter_articles_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Тема', 'verbose_name_plural': 'Темы'},
        ),
    ]