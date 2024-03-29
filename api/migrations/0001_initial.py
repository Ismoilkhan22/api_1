# Generated by Django 5.0.1 on 2024-01-26 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telefon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('brand', models.CharField(max_length=128)),
                ('xotira', models.IntegerField()),
                ('xotira_type', models.CharField(choices=[('MB', 'MB'), ('GB', 'GB'), ('TB', 'TB')], max_length=2)),
                ('rangi', models.CharField(choices=[('oq', 'oq'), ('qora', 'qora'), ('kuk', 'kuk')], max_length=10)),
                ('narxi', models.CharField(max_length=128)),
                ('narxi_tipi', models.CharField(choices=[('USD', 'USD'), ('USZ', 'USZ'), ('EUR', 'EUR'), ('RUB', 'RUB')], max_length=3)),
            ],
        ),
    ]
