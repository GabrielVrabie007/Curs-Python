# TASK 1

# Aceasta este prima ta sarcină a lecției legată de float în python

# Creează o variabilă numită `age` și seteaz-o la vârsta ta

# CODUL TĂU VINE MAI JOS:
age = 20

# CODUL TĂU VINE MAI SUS:

# Acum afișează tipul variabilei `age` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age)
# CODUL TĂU VINE MAI SUS:

# Acum asigură-te că variabila `age` este de tipul float.

# CODUL TĂU VINE MAI JOS:
float(age)
print(type(float(age)))
# CODUL TĂU VINE MAI SUS:

# Creează două variabile numite `age2` și `age3` și setează-le la vârsta prietenilor tăi, ambele variabile trebuie să fie de tipul float.

# CODUL TĂU VINE MAI JOS:
age2 = 18.2
age3 = 21.4
# CODUL TĂU VINE MAI SUS:

# Acum afișează suma vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age2 + age3 + age)
# CODUL TĂU VINE MAI SUS:

# Acum afișează diferența vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age3 - age2 - age)
# CODUL TĂU VINE MAI SUS:

# Acum afișează produsul vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age3 * age2 * age)
# CODUL TĂU VINE MAI SUS:

# Acum afișează împărțirea vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age3 / age2 / age)
# CODUL TĂU VINE MAI SUS:

# Acum afișează restul împărțirii vârstelor voastre folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age3 % age2 % age)
# CODUL TĂU VINE MAI SUS:

# Acum afișează rezultatul vârstei tale ridicată la puterea vârstei primului prieten folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(age**age2)
# CODUL TĂU VINE MAI SUS:

# Acum afișează rezultatul vârstei primului prieten împărțită la puterea vârstei celui de-al doilea prieten folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
rez=age2/(age2**age3)
print(rez)
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot pentru această sarcină


# TASK 2


# Aceasta este a doua ta sarcină legată a leciei legate de stringuri în python

# Creează o variabilă numită `name` și seteaz-o la numele tău

# CODUL TĂU VINE MAI JOS:
name="Gabriel"
# CODUL TĂU VINE MAI SUS:

# Acum afișează valoarea variabilei `name` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(name)
# CODUL TĂU VINE MAI SUS:

# Acum creează o nouă variabilă numită `name2` și seteaz-o la valoarea variabilei `name` și afișează valoarea variabilei `name2` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
name2=name
print(name2)
# CODUL TĂU VINE MAI SUS:

# Acum printează ultimul caracter al variabilei `name` folosind indexarea

# CODUL TĂU VINE MAI JOS:
last_char= name[-1]
print(last_char)
# CODUL TĂU VINE MAI SUS:

# Acum printează primele 3 caractere ale variabilei `name` folosind slicing

# CODUL TĂU VINE MAI JOS:
print(name[:3])
# CODUL TĂU VINE MAI SUS:

# Acum printează valoarea variabilei `name` în majuscule folosind metoda `upper`

# CODUL TĂU VINE MAI JOS:
print(name.upper())
# CODUL TĂU VINE MAI SUS:

# Acum printează valoarea variabilei `name` în minuscule folosind metoda `lower`

# CODUL TĂU VINE MAI JOS:
print(name.lower())
# CODUL TĂU VINE MAI SUS:

# Acum printează concatenarea variabilelor `name` și `name2`

# CODUL TĂU VINE MAI JOS:
print(name+name2)
# CODUL TĂU VINE MAI SUS:

# Creează o variabilă `text` și setează-i un text la alegere, cu restricția ca acesta să conțină mai multe rânduri

# CODUL TĂU VINE MAI JOS:
text=("lorem\n ipsum dolor sit\n continuarea este mai lunga")
print(text)
# CODUL TĂU VINE MAI SUS:

# Verifică dacă variabila `text` conține cuvântul `python`

# CODUL TĂU VINE MAI JOS:
if "python" in text:
    print("python is in text")
else:
    print("python is not in text")
# CODUL TĂU VINE MAI SUS:

# Folosește metoda replace pentru a înlocui litera `a` din variabila `text` cu litera `e`

# CODUL TĂU VINE MAI JOS:
text.replace("a","e")
# CODUL TĂU VINE MAI SUS:

# Folosește metoda split pentru a transforma variabila `text` într-o listă de cuvinte

# CODUL TĂU VINE MAI JOS:
#stergem \n din text
new_text=text.replace("\n","")
print(new_text.split(" "))
# CODUL TĂU VINE MAI SUS:

# Creează un f-string care să conțină variabilele `name` și `name2`

# CODUL TĂU VINE MAI JOS:
f_string = f"Numele meu este {name} și numele meu de familie este {name2}!"
print(f_string)
# CODUL TĂU VINE MAI SUS:

# Verifică dacă string-ul creat se termină cu `!`

# CODUL TĂU VINE MAI JOS:
print(f_string.endswith("!"))

# CODUL TĂU VINE MAI SUS:

# Verifică dacă string-ul creat începe cu `Hello`

# CODUL TĂU VINE MAI JOS:
print(f_string.startswith("Hello"))
# CODUL TĂU VINE MAI SUS:

# Identifică indexul unde se află `!` în string-ul creat

# CODUL TĂU VINE MAI JOS:
print(f_string.index("!"))
# CODUL TĂU VINE MAI SUS:

# Identifică indexul unde se află `o` în string-ul creat folosind altă metodă

# CODUL TĂU VINE MAI JOS:
print(f_string.find("o"))
# CODUL TĂU VINE MAI SUS:

# Utilizând format string-uri, creează un string care să conțină variabilele `name` și `name2`

# CODUL TĂU VINE MAI JOS:
full_string="My name is {} and my friend's name is {}".format(name,name2)
# CODUL TĂU VINE MAI SUS:

# Concatenează string-ul creat cu string-ul `text`

# CODUL TĂU VINE MAI JOS:
concatenate=full_string+text
# CODUL TĂU VINE MAI SUS:

# Afișează lungimea string-ului creat

# CODUL TĂU VINE MAI JOS:
print(len(concatenate))
# CODUL TĂU VINE MAI SUS:

# Aceasta a fost tot pentru această sarcină


# TASK 3

# Aceasta este a treia ta sarcină a lecției legată de type conversion și input-ul user-ului în python

# Creează o variabilă numită `number` și atribuie-i valoarea `10`

# CODUL TĂU VINE MAI JOS:
number=10
# CODUL TĂU VINE MAI SUS:

# Acum afișează valoarea variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(number)
# CODUL TĂU VINE MAI SUS:

# Acum cere user-ului să introducă un număr și atribuie acea valoare variabilei `number` și afișeaz-o folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
number=input("Introduceti noua valore pentru variabila number")
print(number)
# CODUL TĂU VINE MAI SUS:

# Acum afișează tipul variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
print(type(number))
# CODUL TĂU VINE MAI SUS:

# Convertește variabila `number` la tipul `float` și afișează tipul variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
float_nr=float(number)
print(float_nr)
# CODUL TĂU VINE MAI SUS:

# Convertește variabila `number` la tipul `str` și afișează tipul variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
str_num=str(number)
print(type(str_num))
# CODUL TĂU VINE MAI SUS:

# Convertește variabila `number` la tipul `bool` și afișează tipul variabilei `number` folosind funcția `print`

# CODUL TĂU VINE MAI JOS:
bool_num=bool(number)
print(type(bool_num))
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot pentru această sarcină
