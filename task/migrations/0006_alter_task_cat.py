# Generated by Django 5.0.1 on 2024-02-12 05:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_category_task_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='task.category'),
        ),
    ]