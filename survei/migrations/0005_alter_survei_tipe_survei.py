# Generated by Django 5.1.2 on 2024-11-12 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survei', '0004_alter_survei_tipe_survei'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survei',
            name='tipe_survei',
            field=models.CharField(choices=[('Lainnya', 'Lainnya'), ('Paper-based', 'Paper-based'), ('Digital', 'Digital')], default='Paper-based', max_length=255),
        ),
    ]
