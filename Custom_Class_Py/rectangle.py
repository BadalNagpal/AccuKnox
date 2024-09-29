class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {'length': self.length}
        yield {'width': self.width}

    def area(self) -> int:
        """Calculate the area of the rectangle."""
        return self.length * self.width
    
    def perimeter(self) -> int:
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.length + self.width)
    
#Example Usage
if __name__=="__main__":
    rectangle = Rectangle(5, 10)
    for dimension in rectangle:
        print(dimension)

    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())