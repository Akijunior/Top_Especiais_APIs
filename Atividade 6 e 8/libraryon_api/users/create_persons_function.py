from django.contrib.auth.models import User
from users.models import *


def create_users():
    User.objects.create_user('JK_Howling', 'hp@hp.com', '12345')
    User.objects.create_user('Peter', 'pe@pe.com', '12345')
    User.objects.create_user('Gui', 'gi@gi.com', '12345')
    User.objects.create_user('Bia', 'bia@bia.com', '12345')
    User.objects.create_user('C', 'c@c.com', '12345')
    User.objects.create_user('D', 'd@d.com', '12345')

    User.objects.create_user('Cal', 'cal@cal.com', '12345')
    User.objects.create_user('Pete', 'pt@pt.com', '12345')
    User.objects.create_user('Guib', 'gib@gib.com', '12345')
    User.objects.create_user('Bianca', 'bc@bc.com', '12345')
    User.objects.create_user('Cida', 'cd@cd.com', '12345')
    User.objects.create_user('Dani', 'dn@dn.com', '12345')


def create_authors():
    a = User.objects.all()

    Author.objects.create(name='Digns', age=45, email='dig@g.com', password='12345', auth_profile=a[1])
    Author.objects.create(name='Marta', age=55, email='mart@g.com', password='12345', auth_profile=a[2])
    Author.objects.create(name='Guila', age=35, email='gl@g.com', password='12345', auth_profile=a[3])
    Author.objects.create(name='Beatriz', age=25, email='be@g.com', password='12345', auth_profile=a[4])
    Author.objects.create(name='Cardoso', age=40, email='ca@g.com', password='12345', auth_profile=a[5])
    Author.objects.create(name='Diana', age=42, email='di@d.com', password='12345', auth_profile=a[6])


def create_lectors():
    a = User.objects.all()

    Lector.objects.create(name='Kal El', age=15, email='ke@g.com', password='12345', lector_profile=a[7])
    Lector.objects.create(name='Peter Johnson', age=35, email='pj@g.com', password='12345', lector_profile=a[8])
    Lector.objects.create(name='Guiba', age=18, email='gb@g.com', password='12345', lector_profile=a[9])
    Lector.objects.create(name='Bianca', age=25, email='bin@g.com', password='12345', lector_profile=a[10])
    Lector.objects.create(name='Cidane', age=33, email='cid@g.com', password='12345', lector_profile=a[11])
    Lector.objects.create(name='Daniela', age=44, email='dan@g.com', password='12345', lector_profile=a[12])







