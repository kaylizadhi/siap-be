# Generated by Django 4.2.16 on 2024-11-03 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survei', '0004_alter_survei_tipe_survei'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survei',
            name='tipe_survei',
            field=models.CharField(choices=[('Digital', 'Digital'), ('Lainnya', 'Lainnya'), ('Paper-based', 'Paper-based')], default='Paper-based', max_length=255),
        ),
    ]
