# Generated by Django 2.2.16 on 2020-09-15 09:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_board_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board',
            options={},
        ),
        migrations.RemoveField(
            model_name='board',
            name='status',
        ),
    ]