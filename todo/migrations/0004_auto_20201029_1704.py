# Generated by Django 3.1.1 on 2020-10-29 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_task_closed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='size',
            field=models.IntegerField(choices=[(1, 'Trivial'), (2, 'Pequeña'), (3, 'Normal')], default=3),
        ),
    ]
