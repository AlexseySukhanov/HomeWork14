class ProperFraction:
    def __init__(self, numer, denominat):
        if numer >= denominat:
            raise TypeError(f'{numer} is bigger than {denominat} , fraction os not proper!')

        self.numer = numer
        self.denominat = denominat

    def __str__(self):
        return f'{self.numer} / {self.denominat}'

    def __gt__(self, other):
        if not isinstance(self, ProperFraction):
            raise TypeError(f'{type(self).__name__} Object is not valid')
        if not isinstance(other, ProperFraction):
            raise TypeError(f'{type(other).__name__} Object is not valid')
        return self.numer/self.denominat > other.numer/other.denominat

    def __lt__(self, other):
        if not isinstance(self, ProperFraction):
            raise TypeError(f'{type(self).__name__} Object is not valid')
        if not isinstance(other, ProperFraction):
            raise TypeError(f'{type(other).__name__} Object is not valid')
        return self.numer / self.denominat < other.numer / other.denominat

    def __eq__(self, other):
        if not isinstance(self, ProperFraction):
            raise TypeError(f'{type(self).__name__} Object is not valid')
        if not isinstance(other, ProperFraction):
            raise TypeError(f'{type(other).__name__} Object is not valid')
        if self.numer == other.numer:
            return self.denominat == other.denominat

    def __ne__(self, other):
        if not isinstance(self, ProperFraction):
            raise TypeError(f'{type(self).__name__} Object is not valid')
        if not isinstance(other, ProperFraction):
            raise TypeError(f'{type(other).__name__} Object is not valid')
        if self.numer != other.numer:
            return self.denominat != other.denominat

    def __add__(self, other):
        if not isinstance(self, ProperFraction):
            raise TypeError(f'{type(self).__name__} Object is not valid')
        if not isinstance(other, ProperFraction):
            raise TypeError(f'{type(other).__name__} Object is not valid')
        if self.denominat == other.denominat:
            return f'{self.numer + other.numer} / {self.denominat}'
        return f'{self.numer * other.denominat + other.numer * self.denominat} / {self.denominat * other.denominat}'

    def __sub__(self, other):
        if not isinstance(self, ProperFraction):
            raise TypeError(f'{type(self).__name__} Object is not valid')
        if not isinstance(other, ProperFraction):
            raise TypeError(f'{type(other).__name__} Object is not valid')
        if self.denominat == other.denominat:
            return f'{self.numer - other.numer} / {self.denominat}'
        return f'{self.numer * other.denominat - other.numer * self.denominat} / {self.denominat * other.denominat}'

    def __mul__(self, other):
        if not isinstance(self, ProperFraction):
            raise TypeError(f'{type(self).__name__} Object is not valid')
        if not isinstance(other, ProperFraction):
            raise TypeError(f'{type(other).__name__} Object is not valid')
        return f'{self.numer * other.numer} / {self.denominat * other.denominat}'

