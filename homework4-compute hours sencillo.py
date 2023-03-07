def computepay():
    hrs = input("Enter Hours:")
    try: 
        h=float(hrs)
    except:
        print("Please enter a number")
        exit()
    
    rat = input("Enter Rate:")
    try: 
        r=float(rat)
    except:
        print("Please enter a number")
        exit()
    
    if h>40:
        r=r*1.5
        p=str(h*r)
        print("Pay", p)
    else:
        return

computepay()
