# Generated by Django 4.2.16 on 2024-11-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buatAkun', '0002_alter_buatakun_name_alter_buatakun_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='buatakun',
            name='security_answer',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='buatakun',
            name='security_question',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='buatakun',
            name='role',
            field=models.CharField(choices=[('Eksekutif', 'Eksekutif'), ('Admin Sistem', 'Admin Sistem'), ('Administrasi', 'Administrasi'), ('Logistik', 'Logistik'), ('Pengendali Mutu', 'Pengendali Mutu')], max_length=50),
        ),
    ]
