# Generated by Django 3.2.13 on 2022-11-22 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journals', '0002_alter_journal_journal_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='journal_image',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m/%d'),
        ),
    ]
