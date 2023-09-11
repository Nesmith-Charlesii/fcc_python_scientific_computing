class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

    def __str__(self) -> str:
        if self.width == self.height:
            return f'Square(width={self.width}, height={self.height})'
        else: return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self):
        pass

    def set_height(self):
        pass

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
        
        lines = self.height
        plus_signs = self.width
    
    def get_amount_inside(self, shape):
        pass

shape = Rectangle(5,10)
print(shape)



class Square:
    pass