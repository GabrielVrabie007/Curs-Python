
#TODO TASK 1
print("\n***********TASK 1************\n")
# Aceasta este prima ta sarcină legată de liste

# Creează o listă goală numită `numbers`

# CODUL TĂU VINE MAI JOS:
numbers=[]
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numerele de la 1 la 5 în lista `numbers`

# CODUL TĂU VINE MAI JOS:
for i in range(1,6):
    numbers.append(i)

# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numărul 6 la lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.append(6)

# CODUL TĂU VINE MAI SUS:
print(numbers)
# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum șterge numărul 3 din lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.remove(3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum sortează lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.sort()
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`
print(numbers)
# CODUL TĂU VINE MAI JOS:

# CODUL TĂU VINE MAI SUS:

# Acum inversează lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.reverse()
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum afișează lungimea listei `numbers`

# CODUL TĂU VINE MAI JOS:
print(len(numbers))
# CODUL TĂU VINE MAI SUS:

# Acum selectează primele două elemente din lista `numbers` și afișează-le

# CODUL TĂU VINE MAI JOS:
print(numbers[:2])
# CODUL TĂU VINE MAI SUS:

# Acum selectează ultimele trei elemente din lista `numbers` și afișează-le

# CODUL TĂU VINE MAI JOS:
print(numbers[:3])
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numărul 3 la poziția 2 în lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.insert(2,3)
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Creează o listă goală numită `numbers2`

# CODUL TĂU VINE MAI JOS:
numbers2=[]
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numerele de la 6 la 10 în lista `numbers2`

# CODUL TĂU VINE MAI JOS:
for i in range(6,11):
    numbers2.append(i)
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers2`

# CODUL TĂU VINE MAI JOS:
print(numbers2)
# CODUL TĂU VINE MAI SUS:

# Acum adaugă lista `numbers2` la lista `numbers`

# CODUL TĂU VINE MAI JOS:
numbers.extend(numbers2)
# CODUL TĂU VINE MAI SUS:

# Acum afișează lista `numbers`

# CODUL TĂU VINE MAI JOS:
print(numbers)
# CODUL TĂU VINE MAI SUS:

# Acum transformă lista `numbers` într-un string și afișează-l

# CODUL TĂU VINE MAI JOS:
list_as_string=""
for i in numbers:
    list_as_string +=str(i)

print(list_as_string)

# CODUL TĂU VINE MAI SUS:

# Asta a fost tot, ai terminat prima ta sarcină legată de liste