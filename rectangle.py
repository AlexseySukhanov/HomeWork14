class Rectangle:
    def __init__(self, width, heigth):
        self.w = width
        self.h = heigth

    def __str__(self):
        return str(self.w * self.h)

    def __gt__(self, other):
        if not isinstance(self, Rectangle):
            raise TypeError(f'{type(self).__name__} Object is not valid')
        if not isinstance(other, Rectangle):
            raise TypeError(f'{type(other).__name__} Object is not valid')
        return self.w * self.h > other.w * other.h

    def __lt__(self, other):
        if not isinstance(self, Rectangle):
            raise TypeError(f'{type(self).__name__} Object is not valid')
        if not isinstance(other, Rectangle):
            raise TypeError(f'{type(other).__name__} Object is not valid')
        return self.w * self.h < other.w * other.h

    def __eq__(self, other):
        if not isinstance(self, Rectangle):
            raise TypeError(f'{type(self).__name__} Object is not valid')
        if not isinstance(other, Rectangle):
            raise TypeError(f'{type(other).__name__} Object is not valid')
        return self.w * self.h == other.w * other.h

    def __ne__(self, other):
        if not isinstance(self, Rectangle):
            raise TypeError(f'{type(self).__name__} Object is not valid')
        if not isinstance(other, Rectangle):
            raise TypeError(f'{type(other).__name__} Object is not valid')
        return self.w * self.h != other.w * other.h

    def __add__(self, other):
        if not isinstance(self, Rectangle):
            raise TypeError(f'{type(self).__name__} Object is not valid')
        if not isinstance(other, Rectangle):
            raise TypeError(f'{type(other).__name__} Object is not valid')
        return self.w * self.h + other.w * other.h

    def __mul__(self, other):
        if not isinstance(self, Rectangle):
            raise TypeError(f'{type(self).__name__} Object is not valid')
        if not isinstance(other, (int,float)):
            raise TypeError(f'{type(other).__name__} Multipyer is not valid')
        return self.w * self.h * other