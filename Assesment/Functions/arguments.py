#program for Default Arguments
def add(x,y=500):
    "Calculate percentage for 10th mark"
    return str(x/500*100) + "%"
n= int(input("Enter the Mark that you Gained in 10th Standard: "))
print(add(n))
print(add.__doc__)