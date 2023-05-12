class AreaRectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura
    
    # def show_area(self):
    #     print(f"width is: {self.base}")
    #     print(f"height is: {self.altura}")
    #     print(f"area of rectangulo is: {AreaRectangulo.area()}")

width =int(input("what is width? "))
height = int(input("what is height?"))

rect1 = AreaRectangulo(width,height)
print(F"area of rectangulo is: {rect1.area()}")
