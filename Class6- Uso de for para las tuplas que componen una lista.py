#Aplicar el for para una tupla a,b

jjj={'Money': 12, 'Candy': 5, 'Tissues': 75}
for a,b in jjj.items():
    print(a,b)


#Contar las veces que se repitió una palabra, luego decir cual es la más repetida y cuantas veces

Name=input("Enter file: ")
archivo=open(Name)

counts=dict()
for line in archivo:
    words=line.split()
    for word in words:
        counts[word]=counts.get(word,0)+1

#El numero más repetido se llama rep
#El numero de veces que se repite es num

rep=None
num=None

for word,count in counts.items():
    if num is None or count>num:
        rep=word
        num=count

print(rep,num)
