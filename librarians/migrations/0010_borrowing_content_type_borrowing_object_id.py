# Generated by Django 5.1.1 on 2024-11-05 05:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('librarians', '0009_board_game_book_cd_dvd_remove_borrowing_media_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowing',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype'),
        ),
        migrations.AddField(
            model_name='borrowing',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
