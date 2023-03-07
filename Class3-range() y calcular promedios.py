friends= ["Carlos","Juan","Roberto"]
print(friends[2])

lista2= "Hello world"
print(len(lista2))

#Aplicando la función range()

amigos= ["Carlos","Juan","Roberto"]
print(len(amigos))
print(range(4))

print(range(len(amigos)))




#Otra forma de usar for para un rango de datos
for i in range(len(amigos)):
    amigo=amigos[i]
    print("Happy new year:",amigo)


#Cómo calcular un promedio con un input

total=0
count=0

while True:
    inp=input("Enter a number: ")
    if inp=="done":
        break
    value=float(inp)
    total=total+value
    count=count+1

average= total/count
print("Average:",average)


#Calcular un promedio con input pero en lista y con las funciones sum() para sumar y len() para saber la cantidad de datos

total=0
count=0
lista=list()

while True:
    inp=input("Enter a number: ")
    if inp=="done":
        break
    value=float(inp)
    lista.append(value)

average= sum(lista)/len(lista)
print("Average:",average)