# Generated by Django 5.1.1 on 2024-11-23 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarians', '0013_remove_board_game_borrowing_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board_game',
            name='type',
            field=models.CharField(default='Jeu de plateau', max_length=15),
        ),
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.CharField(default='Livre', max_length=15),
        ),
        migrations.AlterField(
            model_name='cd',
            name='type',
            field=models.CharField(default='CD', max_length=15),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='type',
            field=models.CharField(default='DVD', max_length=15),
        ),
    ]
