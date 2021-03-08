# Generated by Django 2.1 on 2020-05-26 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operation',
            name='op_type',
            field=models.CharField(choices=[('ADD', 'ADD'), ('DELETE', 'DELETE'), ('UPDATE', 'UPDATE'), ('LINK', 'LINK'), ('UNLINK', 'UNLINK')], help_text='Operation type (`ADD`, `DELETE` or `UPDATE`)', max_length=128),
        ),
    ]