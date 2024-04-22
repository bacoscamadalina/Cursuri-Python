# VARIANTA 1 - daca in fisier am fi avut mai multe clase, am importat doar clasa Dog si Beagle
print('VARIANTA 1')

from dog import Dog
from beagle import Beagle

d = Dog()
b = Beagle()

d.bark()
b.bark()

# VARIANTA 2 - in acest caz importam intregul modul (importam din toate clasele)
print('VARIANTA 2')

import dog
import beagle

d = dog.Dog()
b = beagle.Beagle()

d.bark()
b.bark()

# VARIANTA 3 - si aceasta este folosita pentru a importa tot modulul
print('VARIANTA 3')

import dog as D  # dupa as putem pune orice prescurtare dorim
import beagle as B

d = D.Dog()
b = B.Beagle()

d.bark()
b.bark()

# VARIANTA 4 - asemanator variantei 2
print('VARIANTA 4')

from dog import *
from beagle import *

d = Dog()
b = Beagle()

d.bark()
b.bark()
