from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import datetime


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class FormUczen(forms.Form):
    imie = forms.CharField(label='Imię:' ,max_length=80)
    imie2 = forms.CharField(laberl='Drugie imię:', max_length=80, required=False)
    nazwisko = forms.CharField(label='Nazwisko:', max_length=80)
    # img = forms.ImageField()

    choices_old = [
        ('LO', 'Liceum Ogólnokształcące'),
        ('ZSZ', 'Zasadnicza Szkoła Zawodowa'),
        ('BS1', 'Branżowa Szkoła I stopnia'),
        ('SP', 'Szkoła Podstawowa')
               ]
    ukonczona_szkola = forms.ChoiceField(label='Ostatnio ukończona szkoła:', choices=choices_old)
    choices_y = []
    for y in range(datetime.datetime.now().year - 100, datetime.datetime.now().year):
        choices_y.append((y, y))     # Tuple!!
    rok_ukonczenia = forms.IntegerField(label='Rok jej ukończenia:', max_length=4, choices=choices_y, default=datetime.datetime.now().year)

    # Kwestionariusz osobowy.
    pesel = forms.IntegerField(label='Pesel:', max_length=9)
    miejsce_urodzenia = forms.CharField(label='Miejsce urodzenia:', max_length=200)
    wojewodztwa = [
        ('DS', 'Dolnośląskie'),
        ('KP', 'Kujawsko-Pomorskie'),
        ('LB', 'Lubelskie'),
        ('LS', 'Lubiskie'),
        ('LD', 'Łódzkie'),
        ('MP', 'Małopolskie'),
        ('MZ', 'Mazowieckie'),
        ('OP', 'Opolskie'),
        ('PK', 'Podkarpackie'),
        ('PL', 'Podlaskie'),
        ('PM', 'Pomorskie'),
        ('SL', 'Śląskie'),
        ('SK', 'Świętokrzyskie'),
        ('WM', 'Warmińsko-Mazurskie'),
        ('WP', 'Wielkopolskie'),
        ('ZP', 'Zachodniopomorskie'),
    ]
    wojewodztwo = forms.ChoiceField(label='Województwo:', choices=wojewodztwa)

    # Adres zamieszkania.
    kod_pocztowy = forms.CharField(label="Kod pocztowy:", max_length=6)
    poczta = forms.CharField(label="Poczta:", max_length=100)
    miejscowosc = forms.CharField(label='Miejscowość:', max_length=100)
    wojewodztwo_ur = forms.ChoiceField(label="Województwo:", choices=wojewodztwa)
    ulica = forms.CharField(label='Ulica:', max_length=100)
    nr_domu = forms.CharField(label='"Numer domu:', max_length=4)
    nr_lokalu = forms.IntegerField(label='Numer lokalu:', max_length=3, required=False)
    email = forms.EmailField(label='Adres email:')
    telefon = forms.IntegerField(label='Numer telefonu:', max_length=11)

    # Opiekunowie.
    matka_imie = forms.CharField(label='Imię matki/prawnej opiekunki:', max_length=80)
    matka_nazwisko = forms.CharField(label='Nazwisko matki/prawnej opiekunki:', max_length=80)
    czy_matka = forms.BooleanField(label='Zaznaczyć, jeśli chodzi o rodzica, a nie o opiekuna.', required=True)
    ojciec_imie = forms.CharField(label='Imię ojca/prawnego opiekuna:', max_length=80)
    ojciec_nazwisko = forms.CharField(label='Nazwisko ojca/prawnego opiekuna:', max_length=80)
    czy_ojciec = forms.BooleanField(label='Zaznaczyć, jeśli chodzi o rodzica, a nie o opiekuna.', required=True)



