# Generated by Django 5.0.1 on 2024-01-24 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_tbl_complainttype'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tbl_category',
        ),
        migrations.DeleteModel(
            name='tbl_complainttype',
        ),
    ]
