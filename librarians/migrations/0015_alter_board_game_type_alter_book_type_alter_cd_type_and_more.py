# Generated by Django 5.1.1 on 2024-11-24 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarians', '0014_alter_board_game_type_alter_book_type_alter_cd_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board_game',
            name='type',
            field=models.CharField(default='board_game', max_length=15),
        ),
        migrations.AlterField(
            model_name='book',
            name='type',
            field=models.CharField(default='book', max_length=15),
        ),
        migrations.AlterField(
            model_name='cd',
            name='type',
            field=models.CharField(default='cd', max_length=15),
        ),
        migrations.AlterField(
            model_name='dvd',
            name='type',
            field=models.CharField(default='dvd', max_length=15),
        ),
    ]
