class person:
    def __init__(self,name,lastname,age):
        self.name = name
        self.lastname = lastname
        self.age = age
    def mostrar_detalle(self):
        print(f"person: {self.name} {self.lastname} {self.age}")

person1 = person('pedro','huiza',24)
person1.mostrar_detalle()

person2 = person('jhayro','loza',25)
person2.mostrar_detalle()





