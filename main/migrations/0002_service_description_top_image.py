# Generated by Django 4.2.7 on 2023-11-09 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='description_top_image',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
