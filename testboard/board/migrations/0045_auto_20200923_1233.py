# Generated by Django 2.2.16 on 2020-09-23 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0044_auto_20200923_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='history', to='board.Board'),
        ),
    ]
