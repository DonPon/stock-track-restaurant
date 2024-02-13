# Generated by Django 4.2.8 on 2024-02-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.TextField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('bought_from', models.CharField(max_length=10)),
                ('bought_on', models.DateField()),
                ('gst_applied', models.CharField(default='', max_length=15)),
                ('price', models.IntegerField(default='', max_length=15)),
                ('ref', models.FloatField()),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]