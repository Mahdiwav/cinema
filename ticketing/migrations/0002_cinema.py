# Generated by Django 5.0 on 2023-12-20 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('cinema_code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(default='تهران', max_length=100)),
                ('capacity', models.IntegerField()),
                ('phone', models.CharField(max_length=50, null=True)),
                ('address', models.TextField()),
            ],
        ),
    ]
