from django.contrib.auth.models import User
from django.db import models
import datetime


class FormUcznia(models.Model):

    imie = models.CharField(max_length=80)
    imie2 = models.CharField(max_length=80, blank=True)
    nazwisko = models.CharField(max_length=80)
    uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE)

    ukonczona_szkola = models.CharField(max_length=3)
    rok_ukonczenia = models.IntegerField(default=datetime.datetime.now().year)

    pesel = models.IntegerField()
    miejsce_urodzenia = models.CharField(max_length=200)
    wojewodztwo = models.CharField(max_length=2)

    kod_pocztowy = models.CharField(max_length=6)
    poczta = models.CharField(max_length=100)
    miejscowosc = models.CharField(max_length=100)
    wojewodztwo_ur = models.CharField(max_length=100)
    ulica = models.CharField(max_length=100)
    nr_domu = models.CharField(max_length=4)
    nr_lokalu = models.IntegerField(null=True)


    def __str__(self):
        return f'Uczeń/Uczennica {self.nazwisko} {self.imie}'
