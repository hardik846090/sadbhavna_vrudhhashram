# Generated by Django 3.1.7 on 2021-03-01 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadbhavna', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatWeDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='whatwedo')),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
