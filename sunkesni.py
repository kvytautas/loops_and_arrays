# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais vienoje eilutėje ir suskaičiuokite kiek tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.
print("-------- 1 --------")

import random

numbers1 = []
count1 = 0

# for i in range(300):
#     numbers.append(random.randint(0, 300))
#     if numbers[i] > 150:
#         count1 += 1

for i in range(300):
    n = random.randint(0, 300)
    if n > 275:
        numbers1.append(f"[{n}]")
    else:
        numbers1.append(str(n))
    if n > 150:
        count1 += 1


print(numbers1)
print(*numbers1, sep=" ", end="\n")
print(count1)


# print("--------")
# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos. Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.

print("-------- 2 --------")

numbers2 = []

for i in range(3000):
    if i % 77 == 0:
        numbers2.append(str(i))

print(numbers2)
print(*numbers2, sep=",", end="")


# Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.
print("-------- 3 --------")
print("-------- 3 --------")

square3 = 25

for i in range(square3):
    print("*"* square3)

# Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu.
print("-------- 4 --------")

square3 = 25

for i in range(square3):
    for j in range(square3):
        if i == j or i + j == square3 - 1: # istrizaine1 arba istrizaine2
            print(" ", end="")
        else:
            print("*", end="")
    print()


# Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius. Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas. Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:
# Iškritus herbui;
# Tris kartus iškritus herbui;
# Tris kartus iš eilės iškritus herbui;
print("-------- 5 --------")

while True:
    dice = random.randint(0,6)
    print(dice)
    if dice == 6:
        break