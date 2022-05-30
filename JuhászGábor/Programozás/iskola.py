
szam = int(input("Hány hetet jártunk ebben a tanévban iskolába?"))


hetek = 36

marad = hetek-szam

print("Ennyi hét van még hátra a tanév végéig!:", marad)

if marad > 5:
    print("Még van idő javítani!")
elif marad<=5:
    print("Itt az év vége!")
elif marad !=int:
    print("Hibás adatot adott meg!")