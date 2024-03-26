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
    def __init__(self, sides: int) -> None:
        self.sides: int = sides
        self.vertices: list = self.build_vertices(sides)
        self.shape_type = None

    def build_vertices(self, sides: int):
        vertices = []
        for _ in range(sides):
            vertices.append(Vertice())

        # Goes backwards through the vertices and connects them.
        # This was simplified from the previous code, now using only one for loop and having a complexity of O(N)
        # Compared to the previous code that had a complexity of O(N^2)
        for i in range(len(vertices)):
            vertices[-i].connect_to(vertices[-i - 1])

        return vertices

    def get_shape(self) -> str:
        functions = ShapeClassifier.get_funtions_to_use(self)
        for function in functions:
            if function(self):
                return function.__name__.replace("is_", "")


class ShapeClassifier:
    @staticmethod
    def get_funtions_to_use(shape: Shape) -> list:
        # Bit of a warning here, this is a very bad way to do this, so
        # if you can figure something out, that would be great.

        # This way you should give priorities to the checks which are more specific.
        # Like, an equilateral check comes before an isoceles check
        # because an equilateral is also an isoceles.
        functions = [ShapeClassifier.is_regular]
        if shape.sides == 3:
            functions.append(ShapeClassifier.is_right_triangle)
        return functions
    @staticmethod
    def is_right_triangle(shape: Shape) -> bool:
        if shape.sides != 3:
            return False

        for vertice in shape.vertices:
            if len(vertice.connected_to) != 2:
                return False
        
        # Check if the Pythagorean theorem applies to the shape
        for vertice in shape.vertices:
            connected_vertices = vertice.connected_to
            a = connected_vertices[0]
            b = connected_vertices[1]
            c = vertice
            if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
                return True
        
        return False

    @staticmethod
    def is_regular(shape: Shape) -> bool:

        #Check if all the sides of the shape are equal
        for vertice in shape.vertices:
            connected_vertices = vertice.connected_to
            for connected_vertice in connected_vertices:
                if connected_vertice != connected_vertices[0]:
                    return False

        return True
    
    #Add more methods here later on