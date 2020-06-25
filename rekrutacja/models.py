from django.contrib.auth.models import User
from django.db import models


class FormUcznia(models.Model):

    imie = models.CharField(max_length=80)
    imie2 = models.CharField(max_length=80, blank=True)
    nazwisko = models.CharField(max_length=80)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)

    # ukonczona_szkola = (
    #     ('LO', 'Liceum Ogólnokształcące'),
    #     ('ZSZ', 'Zasadnicza Szkoła Zawodowa'),
    #     ('BS1', 'Branżowa Szkoła I stopnia'),
    #     ('SP', 'Szkoła Podstawowa')
    # )

    def __str__(self):
        return f'Uczeń/Uczennica {self.nazwisko} {self.imie}'
