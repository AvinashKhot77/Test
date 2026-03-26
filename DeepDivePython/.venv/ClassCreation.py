class rectangle:
    def __init__(self,width,height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,width):
        if width<0:
            raise ValueError
        else:
            self._width=width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self,height):
        if height<0:
            raise ValueError
        else:
            self._height=height

    def __str__(self):
        return 'reactangle ({0},{1})'.format(self._width,self.height)

r1 = rectangle(10,20)
r1.height = 100
print(r1)
