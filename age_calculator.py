# Age Calculator
class person:

    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def age_calculate(self):
        age = 0
        current_year = 2025
        
        for i in range(self.date_of_birth, current_year):
            age += 1

        return f"{self.name} is {age} years old."

obj = person(name = input("Enter your name: "),
            country = input("Enter your country: "), 
            date_of_birth = int(input("Enter your birth year: ")))

print(obj.age_calculate())