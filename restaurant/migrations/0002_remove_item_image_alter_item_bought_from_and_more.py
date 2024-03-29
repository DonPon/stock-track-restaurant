# Generated by Django 4.2.8 on 2024-02-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='image',
        ),
        migrations.AlterField(
            model_name='item',
            name='bought_from',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='item',
            name='bought_on',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='gst_applied',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='item',
            name='ref',
            field=models.FloatField(blank=True),
        ),
    ]
