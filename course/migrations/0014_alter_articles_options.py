# Generated by Django 4.0.1 on 2022-05-18 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_articles_reward'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ('-category',), 'verbose_name': 'Тема', 'verbose_name_plural': 'Темы'},
        ),
    ]
