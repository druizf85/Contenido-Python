c={"a":10,"b":32,"c":21}
tmp=list()
items=c.items()
for k,v in items:
    tmp.append((v,k))

print(tmp)

#Acá me esta ordenando de menor a mayor (por defecto)
tmp=sorted(tmp)

print(tmp)

#Voy a ordenar de mayor a menor usando el reverse=True

tmp=sorted(tmp,reverse=True)

print(tmp)

#Sacar las 10 palabras más comunes en un texto

archivo=open("romeo.txt")
counts=dict()
for line in archivo:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

lst=list()
#Definir el valor mejor
items=counts.items()
for key,value in items:
    newtup=(value,key)
    lst.append(newtup)

lst=sorted(lst,reverse=True)
for value,key in lst[0:10]:
    print(key,value)


#Se puede hacer un codigo de una línea para cambiar key y value y ordenarlos de una vez

c={"a":10,"b":32,"c":21}
items=c.items()
print(sorted([(v,k) for k,v in items]))

print(sorted([(v,k) for k,v in items],reverse=True))

