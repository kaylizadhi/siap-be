# Generated by Django 5.1.1 on 2024-11-30 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survei', '0019_alter_survei_tipe_survei'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survei',
            name='tipe_survei',
            field=models.CharField(choices=[('Lainnya', 'Lainnya'), ('Paper-based', 'Paper-based'), ('Digital', 'Digital')], default='Paper-based', max_length=255),
        ),
    ]
