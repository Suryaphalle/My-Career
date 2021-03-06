# Generated by Django 2.0 on 2018-08-20 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_award'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='facebook',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='linkedin',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='twitter',
            field=models.URLField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.URLField(default='', max_length=100),
        ),
    ]
