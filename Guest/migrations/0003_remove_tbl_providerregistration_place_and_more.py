# Generated by Django 5.0.1 on 2024-02-22 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0002_alter_tbl_user_user_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_providerregistration',
            name='place',
        ),
        migrations.RemoveField(
            model_name='tbl_providerregistration',
            name='providertype',
        ),
        migrations.RemoveField(
            model_name='tbl_user',
            name='place',
        ),
        migrations.DeleteModel(
            name='tbl_freelancer',
        ),
        migrations.DeleteModel(
            name='tbl_providerregistration',
        ),
        migrations.DeleteModel(
            name='tbl_user',
        ),
    ]
