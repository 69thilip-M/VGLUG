#recursive function
'''n=3
def mul(n):
    if n>1:
        return n*mul(n-1)
    else:
        return n
print(mul(-1))'''
#example
'''d="aaaabbbccddddeef"
def val(d):
    counts={}
    for i in d:
        if i in counts:
            counts[i]+=1
        else:
            counts[i]=1
    return counts
res= val(d)
print(res)'''


#OOPS
class Vehicle:

    purpose="travel"
    def __init__(self,motor,wheelcount,maxmember):
        self.type=motor
        self.wheels=wheelcount
        self.members=maxmember
    def run(self):
        print(self.type)
        
bike=Vehicle("bike",2,3)
#print(bike(self.typeOfObject))
print(bike.purpose)
print(bike.run())
       

