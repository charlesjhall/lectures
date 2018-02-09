from turtle import Turtle
from turtle import Screen

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

def radial_pattern(t: Turtle, n: int, length: int, shape) -> None:
    '''

    :param t: an instance of a Turtle used used to render a radial pattern
    :param n: number of polygons to be drawn in the radial pattern
    :param length: length of one side of the polygon
    :param shape: name of the regular polygon to be drawn in the pattern, for example 'square' or 'octagon'
    :return: None
    '''
    for count in range(n):
        shape(t, length)
        t.left(360 / n)

def main() -> int:
    yertle = Turtle()
    screen = Screen()
    yertle.speed(2000)
    screen.colormode(255)
    yertle.color("blue")
    yertle.up()
    square(yertle, 300)
    hexagon(yertle, 100)
    octagon(yertle, 80)
    triangle(yertle, 300)
    regular_polygon(yertle, 5, 100)
    yertle.down()
    radial_pattern(yertle, 299, 100, octagon)
    screen.exitonclick()

if __name__ == '__main__':
    main()
