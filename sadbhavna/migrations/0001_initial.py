# Generated by Django 3.1.7 on 2021-03-01 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='benner')),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('contact', models.CharField(blank=True, max_length=13, null=True)),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
