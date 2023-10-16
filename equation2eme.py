#Programme qui calcule une equation de deuxieme degres
import math
a=int(input("Veuillez entrer a :"))
b=int(input("Veuillez entrer b :"))
c=int(input("Veuillez entrer c :"))
x1=0
x2=0
d=math.pow(b,2) - 4*a*c
if(d>0):
    x1=-b-math.sqrt(d) / 2*a
    x1=-b+math.sqrt(d) / 2*a
    print(f"Les solutions sont : {x1} et {x2}")
elif(d==0):
    x1=-b / 2*a
    print(f"La solution est {x1}")
else:
    print("L'equation n'a pas de solution")

