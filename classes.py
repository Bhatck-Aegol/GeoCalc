from __future__ import annotations


class Fractional_number:
    def __init__(self, numerator: int, denominator: int):
        self.numerator = numerator
        self.denominator = denominator
    def __add__(self, number: int):
        return Fractional_number(self.numerator + number * self.denominator, self.denominator)
    def __add__(self, number: Fractional_number):
        if self.denominator == number.denominator:
            return Fractional_number(self.numerator + number.numerator, self.denominator)
        return Fractional_number(self.numerator * number.denominator + number.numerator * self.denominator, self.denominator * number.denominator)
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
        

class Vertice:
    def __init__(self, connected_to: list = None) -> None:
        if connected_to is None: # REALLY IMPORTANT PART
            connected_to = [] # DO NOT DELETE
        self.connected_to: list = connected_to
    def connect_to(self, other_vertice, one_way = False):
        self.connected_to.append(other_vertice)
        if not one_way:
            other_vertice.connected_to.append(self)


class Shape:
    def __init__(self, sides: int, sides_size) -> None:
        self.sides: int = sides
        self.vertices: list = self.build_vertices(sides)
    def build_vertices(self, sides: int):
        vertices = []
        for _ in range(sides):
            vertices.append(Vertice())
        
        for vertice in vertices:
            for other_vertice in vertices:
                if vertice != other_vertice:
                    vertice.connect_to(other_vertice, one_way = True)

        return vertices