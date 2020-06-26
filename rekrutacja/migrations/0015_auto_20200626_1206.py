# Generated by Django 3.0.7 on 2020-06-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rekrutacja', '0014_formucznia_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='formucznia',
            name='czy_matka',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formucznia',
            name='matka_imie',
            field=models.CharField(default='Imie', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formucznia',
            name='matka_nazwisko',
            field=models.CharField(default='Nazwisko', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='formucznia',
            name='telefon',
            field=models.CharField(default='111111111', max_length=20),
            preserve_default=False,
        ),
    ]