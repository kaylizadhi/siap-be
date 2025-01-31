# Generated by Django 4.2.17 on 2024-12-08 17:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('klien', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Survei',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_survei', models.CharField(default='', max_length=255, unique=True)),
                ('waktu_mulai_survei', models.DateTimeField(default=django.utils.timezone.now)),
                ('waktu_berakhir_survei', models.DateTimeField(default=django.utils.timezone.now)),
                ('harga_survei', models.FloatField(default=0)),
                ('ruang_lingkup', models.CharField(choices=[('Provinsi', 'Provinsi'), ('Nasional', 'Nasional'), ('Kota', 'Kota')], default='Nasional', max_length=255)),
                ('wilayah_survei', models.CharField(default='', max_length=255)),
                ('jumlah_responden', models.IntegerField(default=0)),
                ('tipe_survei', models.CharField(choices=[('Lainnya', 'Lainnya'), ('Digital', 'Digital'), ('Paper-based', 'Paper-based')], default='Paper-based', max_length=255)),
                ('klien', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='survei_set', to='klien.dataklien')),
            ],
            options={
                'db_table': 'survei',
            },
        ),
    ]
