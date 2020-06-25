from django.contrib.auth.models import User
from django.db import models
import datetime


class FormUcznia(models.Model):

    imie = models.CharField(max_length=80)
    imie2 = models.CharField(max_length=80, blank=True)
    nazwisko = models.CharField(max_length=80)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)

    szkoly = (
        ('LO', 'Liceum Ogólnokształcące'),
        ('ZSZ', 'Zasadnicza Szkoła Zawodowa'),
        ('BS1', 'Branżowa Szkoła I stopnia'),
        ('SP', 'Szkoła Podstawowa')
    )
    ukonczona_szkola = models.CharField(max_length=3, choices=szkoly)
    rok_ukonczenia = models.IntegerField(max_length=4, default=datetime.datetime.now().year)

    def __str__(self):
        return f'Uczeń/Uczennica {self.nazwisko} {self.imie}'
