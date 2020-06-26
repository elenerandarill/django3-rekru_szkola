from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import FormUcznia
import datetime


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class FormUczen(forms.ModelForm):
    class Meta:
        model = FormUcznia
        fields = [
            'imie', 'imie2', 'nazwisko', 'ukonczona_szkola', 'rok_ukonczenia',
            'pesel', 'miejsce_urodzenia', 'wojewodztwo', 'kod_pocztowy', 'poczta',
            'miejscowosc', 'wojewodztwo_ur', 'ulica', 'nr_domu', 'nr_lokalu', 'email',
            'telefon', 'matka_imie', 'matka_nazwisko', 'czy_matka', 'ojciec_imie',
            'ojciec_nazwisko', 'czy_ojciec',
                  ]

    imie = forms.CharField(label='Imię:', min_length=2, max_length=80)
    imie2 = forms.CharField(label='Drugie imię:', min_length=2, max_length=80, required=False)
    nazwisko = forms.CharField(label='Nazwisko:', min_length=2, max_length=80)

    # img = forms.ImageField()

    choices_szkola = [
        ('LO', 'Liceum Ogólnokształcące'),
        ('ZSZ', 'Zasadnicza Szkoła Zawodowa'),
        ('BS1', 'Branżowa Szkoła I stopnia'),
        ('SP', 'Szkoła Podstawowa')
               ]
    ukonczona_szkola = forms.ChoiceField(label='Ostatnio ukończona szkoła:', choices=choices_szkola)
    choices_y = []
    for y in range(datetime.datetime.now().year - 100, datetime.datetime.now().year + 1):
        choices_y.append((y, y))     # Tuple!!
    rok_ukonczenia = forms.ChoiceField(label='Rok jej ukończenia:', choices=choices_y, initial=choices_y[-1][1])

    # Kwestionariusz osobowy.
    pesel = forms.IntegerField(label='Pesel:', min_value=10000000000, max_value=99999999999)    # Todo jakies
    miejsce_urodzenia = forms.CharField(label='Miejsce urodzenia:', min_length=3, max_length=200)
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
    kod_pocztowy = forms.CharField(label="Kod pocztowy (w formacie 00-000):", min_length=6, max_length=6)
    poczta = forms.CharField(label="Poczta:", max_length=100)
    miejscowosc = forms.CharField(label='Miejscowość:', max_length=100)
    wojewodztwo_ur = forms.ChoiceField(label="Województwo:", choices=wojewodztwa)
    ulica = forms.CharField(label='Ulica:', max_length=100)
    nr_domu = forms.CharField(label='Numer domu:', max_length=4)
    nr_lokalu = forms.IntegerField(label='Numer lokalu:', max_value=999, required=False)
    email = forms.EmailField(label='Adres email:')
    telefon = forms.CharField(label='Numer telefonu:', max_length=20)

    # Opiekunowie.
    matka_imie = forms.CharField(label='Imię matki/prawnej opiekunki:', max_length=80)
    matka_nazwisko = forms.CharField(label='Nazwisko matki/prawnej opiekunki:', max_length=80)
    czy_matka = forms.BooleanField(label='Zaznaczyć, jeśli chodzi o rodzica, a nie o opiekuna.', required=False)
    ojciec_imie = forms.CharField(label='Imię ojca/prawnego opiekuna:', max_length=80)
    ojciec_nazwisko = forms.CharField(label='Nazwisko ojca/prawnego opiekuna:', max_length=80)
    czy_ojciec = forms.BooleanField(label='Zaznaczyć, jeśli chodzi o rodzica, a nie o opiekuna.', required=False)



