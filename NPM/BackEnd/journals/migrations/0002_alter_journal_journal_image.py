# Generated by Django 3.2.13 on 2022-11-22 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='journal_image',
            field=models.FileField(blank=True, null=True, upload_to='%Y/%m/%d'),
        ),
    ]