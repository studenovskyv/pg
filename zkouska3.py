# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte třídu `Shape` s abstraktní metodou `area`.
# Vytvořte dvě podtřídy: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.

from abc import ABC, abstractmethod
import math #Importoval jsem knihovnu math

class Shape(ABC): #Abstract Base Class
    @abstractmethod #dekoder ktery znaci ze to bude abstraktni metorou
    def area(self): #jen implementuje funkci
        pass
# ZDE DOPLŇTE VLASTNÍ KÓD







class Rectangle(Shape):
    def __init__(self, sirka, vyska): #konstruktor odkazujici na aktualni instanci a definuji mu rozmery
        """
        Inicializuje šířku a výšku obdélníku.
        """
        self.width = sirka
        self.height = vyska

    def area(self):
        """
        Vypočítá plochu obdélníku (šířka * výška).
        """
        return self.width * self.height

class Circle(Shape):
    def __init__(self, polomer):
        """
        Inicializuje poloměr kruhu.
        """
        self.polomer = polomer

    def area(self):
        """
        Vypočítá plochu kruhu (pi * r^2).
        """
        return math.pi * (self.polomer ** 2) #pouziju implementovanou knihovnu math a z ni pi







# Pytest testy pro Příklad 3
from unittest.mock import patch, MagicMock, mock_open

def test_shapes():
    rect = Rectangle(4, 5)
    assert rect.area() == 20

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3

    with patch("abc.ABC", side_effect=NotImplementedError):
        try:
            shape = Shape()
        except TypeError:
            pass