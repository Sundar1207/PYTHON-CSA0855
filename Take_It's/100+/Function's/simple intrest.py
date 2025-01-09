"""simple intrest"""
class intrest:
    def __init__(self,y,p,city):
        self.y=y
        self.p=p
        self.i= 12 if city else 10
    def simple(self):
        return (self.y*self.p*self.i)/100
        
p=int(input("Enter the input : "))
y=int(input("Enter the year : "))
city=input("Enter (y/n) : ").strip().upper() == 'Y'

SI=intrest(p,y,city)
calculate=(SI.simple())
print(calculate)
