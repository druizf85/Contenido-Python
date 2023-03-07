#Usar la función split()

line= "Hola mis burros"
etc=line.split()

print(etc)

line2="first;second;third"
etc=line2.split(";")
print(etc)


#ejemplo con archivos de texto
archivo=open("txt.txt")
for line in archivo:
    line=line.rstrip()
    if not line.startswith("from"):
        continue
    words=line.split()
    print(words[2])

#ejemplo con texto normal
texto="From stephen.marcopoloconchetumadre@penelargo.com.mx Sat Jan 5 09:14:16 2008"
words=texto.split()
print(words[2])

#Nombrar partes de un texto y dividirlo
texto="From stephen.marcopoloconchetumadre@penelargo.com.mx Sat Jan 5 09:14:16 2008"
words=texto.split()
email=words[1]
pieces=email.split("@")
print(pieces[1])

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print(friends[0])