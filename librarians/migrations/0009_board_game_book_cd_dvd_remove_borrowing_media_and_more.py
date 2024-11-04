# Generated by Django 5.1.1 on 2024-11-02 14:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarians', '0008_alter_borrowing_borrowing_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board_game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(default='board_game', max_length=15)),
                ('creator', models.CharField(max_length=100)),
                ('available', models.BooleanField(default=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(default='book', max_length=15)),
                ('author', models.CharField(max_length=100)),
                ('borrowing_date', models.DateField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
                ('borrowers_number', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(default='cd', max_length=15)),
                ('artist', models.CharField(max_length=100)),
                ('borrowing_date', models.DateField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
                ('borrowers_number', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dvd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(default='dvd', max_length=15)),
                ('director', models.CharField(max_length=100)),
                ('borrowing_date', models.DateField(blank=True, null=True)),
                ('available', models.BooleanField(default=True)),
                ('borrowers_number', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='borrowing',
            name='media',
        ),
        migrations.AddField(
            model_name='borrowing',
            name='board_game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='librarians.board_game'),
        ),
        migrations.AddField(
            model_name='borrowing',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='librarians.book'),
        ),
        migrations.AddField(
            model_name='borrowing',
            name='cd',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='librarians.cd'),
        ),
        migrations.AddField(
            model_name='borrowing',
            name='dvd',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='librarians.dvd'),
        ),
        migrations.DeleteModel(
            name='Media',
        ),
    ]