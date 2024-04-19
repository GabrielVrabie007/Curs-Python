# Aceasta este tema pentru lecția 8 legată de loops
import math
import random

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
my_list=[]
for i in range(1,11):
    my_list.append(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
for nr in my_list:
    if nr%2==0:
        print(nr)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i=1
while(i<5):
    i+=1
    print(i)
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
my_dict={
     "name":"Gabriel",
     "age":20,
     "city":"New York"
}
for key,value in my_dict.items():
    print(key,value)
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]

for row in matrix:
    print(row)

# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
for i in range(1,21):
    print(i)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
arr_1=["alex","gheorghe","mihai","corina","nastea"]
obj_1=enumerate(arr_1)
print(list(obj_1))
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
arr_2=[True,False,False,True,False]
x=zip(arr_1,arr_2)
print(tuple(x))
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
second_list=[]
for i in range(1,11):
    second_list.append(i)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
second_list = [10, 20, 30, 40, 50]

while second_list[0] <= 50:
    for i in range(len(second_list)):
        second_list[i] *= 2

print(second_list)

# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
perfect_squares=[]
for number in range(1,101):
    sqrt_number=math.sqrt(number)
    if(sqrt_number.is_integer()):
        perfect_squares.append(number)
print(perfect_squares)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for i in range(1,11):
    print("7 x",i,"=",7*i)
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
lista_de_liste = [[(i, j) for j in range(1, 6)] for i in range(1, 6)]

for sublist in lista_de_liste:
    print(sublist)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
for sublist in lista_de_liste:
    for i,j in sublist:
        if(i<j):
            print(lista_de_liste[i-1][j-1])
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
rand_list=[]
for i in range(1,10):
    n=random.randint(0,11)
    rand_list.append(n)

found=False
i=0
while i<len(rand_list):
    if(rand_list[i])>=10:
        print(f"Number {rand_list[i]} was found in list at index {i}")
        found=True
        break
    i+=1
if not found: print("Number>=10 not found in list")


# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
print("Scrie dimensiunea laturii la patrat")
size=int(input())
for i in range(size):
    for j in range(size):
        print("* ",end="")
    print()
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:

num_rows = 7
for i in range(1, num_rows):
    for j in range(1, i + 1):
        print(j, end="")

    print()


# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
num_rows = 6

for i in range(num_rows, 0, -1):
    for j in range(num_rows, num_rows - i, -1):
        print(j, end="")
    print()

# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:


letter_list=["abcdefgh"]
for string in letter_list:
    for i in range(len(string)):
        print(string[i:],end="")
        print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
def is_odd(index):
    if index%2==1:
        return True

str_1=["+-+-+-+-+-+-+-+-"]
str_2=["-+-+-+-+-+-+-+-+"]

i=1
max_print=10
while(i<max_print):
    if(is_odd(i)):
        for text in str_1:
            print(str_1)
            i+=1
    else:
        print(str_2)
        i+=1

# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
number = 3

for i in range(5):
    current_number = number
    for j in range(i + 1):
        print(current_number, end=" ")
        current_number *= 3
    print()

number=3

for i in range(4):
    current_number =number
    for j in range(4-i):
        print(current_number,end=" ")
        current_number*=3
    print()


# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.