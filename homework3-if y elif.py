
#3.3 Write a program to prompt for a score between 0.0 and 1.0 ....


score = input("Enter Score: ")

try: 
    s=float(score)
except:
    print("Please enter a number")
    exit()

if s<0:
    print("Please enter a number between 0.0 and 1.0")
    exit()
elif s>1:
    print("Please enter a number between 0.0 and 1.0")
    exit()

if s>=0.9:
    print("A")
    exit()
if s>=0.8:
    print("B")
    exit()
if s>=0.7:
    print("C")
    exit()
if s>=0.6:
    print("D")
    exit()
if s<0.6:
    print("F")
    exit()





