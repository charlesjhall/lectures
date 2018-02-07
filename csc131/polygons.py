from turtle import Turtle

def square(t: Turtle, length: int):
    """
    Draw a hexagon with a given length
    :param t: an instance of a Turtle used to render a square
    :param length: length of one side of the square
    :return: None
    """
    b=4
    for count in range(b):
        t.forward(length)
        t.left((360/b))

def hexagon(t: Turtle, length: int):
    """
    Draw a hexagon with a given length
    :param t: an instance of a Turtle used used to render a hexagon
    :param length: length of one side of the hexagon
    :return: None
    """
    b=6
    for count in range(b):
        t.forward(length)
        t.left((360/b))

def octagon(t: Turtle, length: int):
    """
    Draw a hexagon with a given length
    :param t: an instance of a Turtle used used to render a octagon
    :param length: length of one side of the octagon
    :return: None
    """
    b=8
    for count in range(b):
        t.forward(length)
        t.left((360/b))

def triangle(t: Turtle, length: int):
    """
    Draw a hexagon with a given length
    :param t: an instance of a Turtle used used to render a triangle
    :param length: length of one side of the triangle
    :return: None
    """
    b=3
    for count in range(b):
        t.forward(length)
        t.left((360/b))

def regular_polygon(t: Turtle, length: int, num_sides=4):
    """
    Draw any regular polygon with a given length
    :param t: an instance of a Turtle used used to render a regular polygon
    :param length: length of one side of the polygon
    :param num_sides: number of sides of the regular polygon
    :return: None
    """
    for count in range(num_sides):
        t.forward(length)
        t.left((360 / num_sides))

def main() -> int:
    yertle = Turtle()
    square(yertle, 300)
    hexagon(yertle, 100)
    octagon(yertle, 80)
    triangle(yertle, 300)
    regular_polygon(yertle, 5, 300)

if __name__ == '__main__':
    main()