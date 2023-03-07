#name=input("cual es tu nombre?")
#print("holitaaa señora",name)


# 2.3 This first line is provided for you

hrs = input("Enter Hours:")

hrs=float(hrs)

rt=input("Enter rate:")
rt=float(rt)

p=rt*hrs

p=str(p)

print("Pay: "+p)


#conditionals

x=1

if x>2:
    print("greater than 2")
print("done with 2")

for y in range(7):
    print(y)
    if y>2:
        print("bigger than 2")
        print("done with y",y)
print("all done")


#Try and except

x="holandaaa"
try:
    y=int(x)
except:
    y=-1
print("First",y)

xx="123"
try:
    yy=int(xx)
except:
    yy=-1
print("Second",yy)


z= input("escriba un numero mayor que cero")
try:
    f=int(z)
except:
    f=-1
if f<0:
    print("mala")
else:
    print("okas")