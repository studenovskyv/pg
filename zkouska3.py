# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.




import math  # Import knihovny pro práci s matematickými funkcemi

class Shape:
    """
    Třída Shape reprezentuje obecný geometrický tvar.
    Obsahuje základní metodu `area`, která vrací 0.0.
    """
    def area(self):
        """
        Vrátí plochu geometrického tvaru.
        (V této základní třídě vrací 0.0, protože konkrétní výpočet
        závisí na podtřídách.)
        """
        return 0.0

# Vytvoření podtřídy `Rectangle`
class Rectangle(Shape):
    """
    Třída Rectangle reprezentuje obdélník.
    """
    def __init__(self, width, height):
        """
        Inicializuje obdélník s šířkou `width` a výškou `height`.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Vypočítá plochu obdélníku jako šířka * výška.
        """
        return self.width * self.height

# Vytvoření podtřídy `Circle`
class Circle(Shape):
    """
    Třída Circle reprezentuje kruh.
    """
    def __init__(self, radius):
        """
        Inicializuje kruh s poloměrem `radius`.
        """
        self.radius = radius

    def area(self):
        """
        Vypočítá plochu kruhu jako π * r^2.
        """
        return math.pi * (self.radius ** 2)






# Pytest testy pro Příklad 3
from unittest.mock import patch, MagicMock, mock_open

def test_shapes():
    """
    Testy ověřují správnost implementace tříd Rectangle a Circle.
    """
    rect = Rectangle(4, 5)
    assert rect.area() == 20  # Plocha obdélníku se šířkou 4 a výškou 5 je 20

    circle = Circle(3)
    assert round(circle.area(), 1) == 28.3  # Plocha kruhu s poloměrem 3 je přibližně 28.3
