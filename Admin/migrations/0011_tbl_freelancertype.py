# Generated by Django 5.0.1 on 2024-02-03 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0010_tbl_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_freelancertype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('freelancertype_name', models.CharField(max_length=50)),
            ],
        ),
    ]
