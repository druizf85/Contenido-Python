#Dictionaries (bags)

purse=dict()
purse["Money"]=12
purse["Candy"]=3
purse["Tissues"]=75

print(purse)

print(purse["Candy"])

purse["Candy"]=purse["Candy"]+2

print(purse)


#Para hacer una cuenta en un dict de los nbombres que pasan y cuantas veces pasan
counts=dict()
names= ["Alberta","Juana","Marimba","Juana","Alex","Juana","Alex"]
for name in names:
    if name not in counts:
        counts[name]=1
    else:
        counts[name]=counts[name]+1

print(counts)

#Aplicando la función get()

counts=dict()
names= ["Alberta","Juana","Marimba","Juana","Alex","Juana","Alex"]
for name in names:
    counts[name]=counts.get(name,0)+1

print(counts)

#Ejercicio práctico con get() y los dict para textos largos
#Cual es la palabra más repetida

counts=dict()
print("Enter a text")
line= input(" ")
words=line.split()
print("Words: ",words)
print("Counting...")
for word in words:
    counts[word]=counts.get(word,0)+1
print("Counts", counts)


#Ejercicio de lists of keys and values
jjj={'Money': 12, 'Candy': 5, 'Tissues': 75}
print(list(jjj))
print(jjj.keys())
print(jjj.values())
print(jjj.items())

#Todas las anteriores entregan la información en tipo lista [] 





