class Car:
    def __init__(self, model, year,color,for_sale):# self คือตัวมันเอง
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"Your drive the {self.model} ")

    def drive(self):
        print(f"Your stop the {self.model} ")

    def describe(self):
        print(f"Your {self.model} ")