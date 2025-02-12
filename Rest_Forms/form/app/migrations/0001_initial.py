# Generated by Django 5.1.4 on 2025-02-12 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('position', models.CharField(max_length=40)),
                ('department', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=12)),
                ('salery', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
