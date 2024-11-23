# Generated by Django 5.1.3 on 2024-11-22 05:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_medicamento_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_emision', models.DateField(auto_now_add=True, verbose_name='Fecha de Emisión')),
                ('motivo', models.TextField(verbose_name='Motivo del Certificado')),
                ('detalles', models.TextField(blank=True, null=True, verbose_name='Detalles del Certificado')),
                ('firmado', models.BooleanField(default=False, verbose_name='Firmado')),
                ('archivo_pdf', models.FileField(blank=True, null=True, upload_to='certificados/', verbose_name='Certificado en PDF')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='certificados', to='core.doctor', verbose_name='Doctor')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificados', to='core.paciente', verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Certificado',
                'verbose_name_plural': 'Certificados',
                'ordering': ['-fecha_emision'],
            },
        ),
    ]
