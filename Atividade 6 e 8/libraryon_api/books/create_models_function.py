from .models import *


def create_books():
    Book.objects.create(title='Digns', description="Slice of life", isbn='1111', edition='5ª Edição',
                        year=2015, amount_pages=350, price=45.90)
    Book.objects.create(title='Leona', description='Fantastic sup', isbn='2222', edition='2ª Edição',
                        year=2018, amount_pages=250, price=35.90, age_range='FT')
    Book.objects.create(title='Nauti', description='Other best sup', isbn='3333', edition='3ª Edição',
                        year=2018, amount_pages=200, price=15.90, age_range='ST')
    Book.objects.create(title='Jarvan', description='Jungle', isbn='4444', edition='4ª Edição',
                        year=2015, amount_pages=350, price=45.90)
    Book.objects.create(title='Bioshock', description='Game', isbn='5555', edition='1ª Edição',
                        year=2010, amount_pages=450, price=75.90)


def create_genres():
    Genre.objects.create(name='Drama', description='Dramático')
    Genre.objects.create(name='Ação', description='Adrenalina')
    Genre.objects.create(name='Terror', description='Assustador')
    Genre.objects.create(name='Romance', description='Romântico')
    Genre.objects.create(name='Comédia', description='Engraçada')








