# Generated by Django 5.0.1 on 2024-02-02 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_task_options_task_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]