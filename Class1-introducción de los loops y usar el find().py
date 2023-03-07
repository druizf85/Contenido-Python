#Strings Part 1

#Letras de banano

fruta="banano"
indice=0
while indice<len(fruta):
    x=fruta[indice]
    print(indice,x)
    indice=indice+1



#Contar letras en una palabra
# los loop son for y while

word="banano"
contar=0
for x in word:
    if x == "a":
        contar=contar+1
print(contar)


#Strings Part 2

#in
fruit="banano"
"z" in fruit

#También se puede usar en if XXX in XX...

cosa="banano"
pos=cosa.find("na")
print(pos)

aa=cosa.find("z")
print(aa)

#Cómo recortar un correo o un pedazo de información

#Sacar un espacio desde un @ oara oider recortar lo que nos ineresa From Steven mcnomalan@cuatro.com.caca sat jan 5 09:14:23 2007

data= "From Steven mcnomalan@cuatro.com.caca sat jan 5 09:14:23 2007"

atpos=data.find("@")
print(atpos)

sppos=data.find(" ",atpos)
print(sppos)

host=data[atpos+1:sppos]

print(host)







