#TODO CLASE   OBIECTE   EXEMPLE DE CLASE

class Airplane:
    name="Boeing 766M"
    flight_time=18
    max_speed=900
    max_people=400

#TODO in afara clasei am definit un nou atribut dinamic
Airplane.pilots=3

#TODO class_name.__dict__ va afisa tot ce se contine in clasa voastra
all_atributes = Airplane.__dict__
print(all_atributes)

#TODO get_atribute     getattr-functie care i-a un atribut aparte din clasa

#200-by default value if atribute is not defined in class
getattr(Airplane, "max_speed",200)

#Am creat un obiect al clasei Airplane
airplane_1=Airplane()
airplane_1.name="SU-57 MAX"
print(airplane_1.name)
print(isinstance(airplane_1,Airplane))
airplane_1.pilots=1

delattr(airplane_1,"max_speed")


#TODO set_atribute  setattr-atribuie la un atribut deja EXISTENT o valoare

setattr(Airplane,"pilots",5)

print(airplane_1.pilots)
print(Airplane.pilots)

#TODO delete_atribute     delattr

delattr(Airplane,"max_people")
#print(Airplane.max_people)----EROARE



