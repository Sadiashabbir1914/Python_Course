class car:

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def start(self):
        print(f"{self.brand} is starting now. . .")

car1 = car("Ferrari", 2026, "Blue & Black")

print(car1.brand)

car1.start()

