# Age Calculator
class person:

    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year

    def age_calculate(self):
        age = 0
        current_year = 2025
        
        try:
            if self.birth_year > current_year:
                raise ValueError("Invalid Year!")
        except ValueError as e:
            return e

        for i in range(self.birth_year, current_year):
            age += 1

        return f"{self.name} is {age} years old."

obj = person(name = input("Enter your name: "),
            country = input("Enter your country: "), 
            birth_year = int(input("Enter your birth year: ")))

print(obj.age_calculate())