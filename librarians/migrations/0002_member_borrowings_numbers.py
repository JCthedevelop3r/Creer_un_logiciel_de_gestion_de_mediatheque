# Generated by Django 5.1.1 on 2024-10-17 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarians', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='borrowings_numbers',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
