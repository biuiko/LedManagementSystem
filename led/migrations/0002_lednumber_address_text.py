# Generated by Django 2.0.13 on 2019-03-17 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('led', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lednumber',
            name='address_text',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
