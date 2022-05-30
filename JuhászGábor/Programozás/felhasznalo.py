import random
class Felhasznalo():
    def __init__(self, vezeteknev,keresztnev):
        self.keresztnev=keresztnev
        self.vezeteknev=vezeteknev
    
    def printname(self):
        y = self.vezeteknev[0]+self.keresztnev[0]
        z = random.randint(100,999)
        k = y+str(z)
        print(k)

x = Felhasznalo(input("Kérem a vezetéknevet!"),input("Kérem a keresztnevet!"))
x.printname()