#Tuples

l=list()
print(dir(l))

t=tuple()
print(dir(t))

d=dict()
d["mama"]=2
d["papa"]=4
d["son"]=54

for a,b in d.items():
    print(a,b)

#Se le asigna un nombre a esta formula aplicada al dict inicial
tups= d.items()
print(tups)


#Comparaciones entre tuples, considera el primer elemento

#Uso de la función sorted() para ordenar por orden alfabético (primer dato siempre)

#Se le asigna un nombre
tups= d.items()
print(tups)

#Se le asigna un nombre
sorted=sorted(tups)

print(sorted)

for a,b in sorted:
    print(a,b)
