# Generated by Django 5.0.6 on 2024-08-06 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bananas', '0009_remove_cutofbanana_numero_lot_alter_cutofbanana_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cutofbanana',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
