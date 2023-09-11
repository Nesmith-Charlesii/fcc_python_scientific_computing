class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = (2 * self.width) + (2 * self.height)
        return perimeter

    def get_diagonal(self):
        # '**' is an operator used for exponentiation 
        diagonal = ((self.width ** 2) + (self.height ** 2)) ** .5
        return diagonal

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        else:
            picture = ""
            for i in range(0, self.height):
                for a in range(0, self.width):
                    picture += "*"
                picture += "\n"
            return picture
    
    def get_amount_inside(self, shape):
        amount_row = self.width / shape.width
        amount_column = self.height / shape.height
        amount_inside = int(amount_column * amount_row)
        return amount_inside


class Square(Rectangle):
    def __init__(self, side) -> None:
        self.width = side
        self.height = side

    def __str__(self) -> str:
        return f'Square(side={self.width})'
    
    def set_side(self, side):
        super().set_height(side)
        super().set_width(side)

    def set_width(self, side):
        super().set_width(side)
        super().set_height(side)
    
    def set_height(self, side):
        super().set_width(side)
        super().set_height(side)
    

rectangle = Rectangle(10,5)
print(rectangle)
print(rectangle.get_area())
rectangle.set_height(3)
print(rectangle.get_perimeter())
print(rectangle)
print(rectangle.get_picture())

square = Square(9)
print(square.get_area())
square.set_side(4)
print(square.get_diagonal())
print(square)
print(square.get_picture())

rectangle.set_height(8)
rectangle.set_width(16)
print(rectangle)
print(square)
print(rectangle.get_amount_inside(square))