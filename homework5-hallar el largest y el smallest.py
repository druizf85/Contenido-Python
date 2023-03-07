largest = None
smallest = None
while True:
    x=input("Enter a number: ")
    if x=="done":
        break
    try:
        n=int(x)
    except:
        print("Invalid input")
    if largest==None and smallest==None:
        largest=n
        smallest=n
    if n > largest:
        largest=n
    if n < smallest:
        smallest=n
print("Maximum is",largest)
print("Minimum is",smallest)
    

