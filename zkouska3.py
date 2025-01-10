# Příklad 3: Základy OOP (dědičnost, abstrakce, zapouzdření)
# Zadání:
# Vytvořte dvě podtřídy třídy `Shape`: `Rectangle` a `Circle`.
# - `Rectangle` má atributy `width` a `height` a implementuje metodu `area`.
# - `Circle` má atribut `radius` a implementuje metodu `area`.




import math 

class Shape:
   
    def area(self):
        
        return 0.0

class Rectangle(Shape):
   
    def __init__(self, width, height):
        
        self.width = width
        self.height = height

    def area(self):
        
        return self.width * self.height

class Circle(Shape):
    
    def __init__(self, radius):
        
        self.radius = radius

    def area(self):
        
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
