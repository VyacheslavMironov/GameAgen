# Generated by Django 4.0.1 on 2022-05-01 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_aboutuser_active_back_aboutuser_active_frame_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutuser',
            name='active_back',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='set_backs', to='main.gameitems'),
        ),
        migrations.AlterField(
            model_name='aboutuser',
            name='active_frame',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='set_frames', to='main.gameitems'),
        ),
    ]
