# Generated by Django 4.2.3 on 2023-07-13 00:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={},
        ),
        migrations.RenameField(
            model_name='task',
            old_name='create',
            new_name='created',
        ),
        migrations.AlterOrderWithRespectTo(
            name='task',
            order_with_respect_to='user',
        ),
    ]
