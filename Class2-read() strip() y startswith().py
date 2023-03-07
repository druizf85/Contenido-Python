 #Files  \n

print ("hello\nWorld")

x= open("mama.txt")
count=0
for line in x:
    count=count+1
print("line count: ",count)

#corriendo el código...
Line count: 132553
#muestra el numero de líneas

#leer el archivo

x= open("mama.txt")
y=x.read()
print(len(y))
#corriendo el código...
94633
print(y[:20])

#corriendo el código...
From Steven Hawkings


#
x= open("mama.txt")
for line in  x:
    if line.startswith("From: "):
        print(line)

#corriendo el código... El print() da un espacio automáticamente
From: Alberto martinez

From Luis Gardiazaval

From: Carlos Alvarado

#Cuando se habla de archivos, la variable en el loop for (line) es una línea
#Se incluye el rstrip

x= open("mama.txt")
for line in  x:
    line=line.rstrip()
    if line.startswith("From: "):
        print(line)

#corriendo el código... El print() da un espacio automáticamente
From: Alberto martinez
From Luis Gardiazaval
From: Carlos Alvarado



#Otra forma de usar, con "in"

x= open("mama.txt")
for line in  x:
    line=line.rstrip()
    if not "Holandaaa" in line:
        continue
    print(line)


#Finalmente, cómo hacer el try except
fname=input("Enter the file name: ")
try:
    x=open(fname)
except:
    print("Ingrese un nombre de archivo valido, este no abre", fname) 
    quit()

count=0
for line in x:
    if line.startswith("Subject: "):
        count=count+1
print("There where: ",count), "Subject lines in",fname)
#corriendo el código...
Enter the file name: Carechimbo
There where 1536485 Subject lines in Carechimbo