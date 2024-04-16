# TODO CLASE   OBIECTE   EXEMPLE DE CLASE

class Airplane:
    name = "Boeing 766M"
    flight_time = 18
    max_speed = 900
    max_people = 400


# TODO in afara clasei am definit un nou atribut dinamic
Airplane.pilots = 3

# TODO class_name.__dict__ va afisa tot ce se contine in clasa voastra
all_atributes = Airplane.__dict__
print(all_atributes)

# TODO get_atribute     getattr-functie care i-a un atribut aparte din clasa

# 200-by default value if atribute is not defined in class
getattr(Airplane, "max_speed", 200)

# Am creat un obiect al clasei Airplane
airplane_1 = Airplane()
airplane_1.name = "SU-57 MAX"
print(airplane_1.name)
print(isinstance(airplane_1, Airplane))
airplane_1.pilots = 1

# delattr(airplane_1,"max_speed")


# TODO set_atribute  setattr-atribuie la un atribut deja EXISTENT o valoare

setattr(Airplane, "pilots", 5)

print(airplane_1.pilots)
print(Airplane.pilots)

# TODO delete_atribute     delattr

delattr(Airplane, "max_people")


# print(Airplane.max_people)----EROARE


class People():
    def __init__(self):
        self.name = "UNKNOWN USER"
        self.job = "UNKNOWN JOB"
        self.age = 0

    def age_until_retirement(self, age) -> int:
        retirement_age = 65
        return retirement_age - age

    def has_job(self):
        if self.age >= 65:
            print(f"{self.name} is retired.")
        elif 18 <= self.age < 65:
            print(f"{self.name} works as a {self.job}.")
        else:
            years_left = 18 - self.age
            print(f"{self.name} has {years_left} years until he/she can have a job.")

Person_1 = People()
Person_1.name = "Gabriel"
Person_1.age = 20
print(Person_1.age_until_retirement(Person_1.age))

Person_2 = People()

print("Introduce your current age:")
Person_2.age = int(input())
Person_2.name = "Andrei"
Person_2.job = "Software Engineer"  # Set a default job
Person_2.has_job()

