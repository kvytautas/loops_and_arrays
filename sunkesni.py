import random
# Sugeneruokite 300 atsitiktinių skaičių nuo 0 iki 300, atspausdinkite juos atskirtus tarpais vienoje eilutėje ir suskaičiuokite kiek tarp jų yra didesnių už 150.  Skaičiai didesni nei 275 turi būti atspausdinti skliausteliuose” [ ] “.
# print("-------- 1 --------")



# numbers1 = []
# count1 = 0

# # for i in range(300):
# #     numbers.append(random.randint(0, 300))
# #     if numbers[i] > 150:
# #         count1 += 1
#
# for i in range(300):
#     n = random.randint(0, 300)
#     if n > 275:
#         numbers1.append(f"[{n}]")
#     else:
#         numbers1.append(str(n))
#     if n > 150:
#         count1 += 1
#
#
# print(numbers1)
# print(*numbers1, sep=" ", end="\n")
# print(count1)


# print("--------")
# Vienoje eilutėje atspausdinkite visus skaičius nuo 1 iki 3000, kurie dalijasi iš 77 be liekanos. Skaičius atskirkite kableliais. Po paskutinio skaičiaus kablelio neturi būti.

# print("-------- 2 --------")
#
# numbers2 = []
#
# for i in range(3000):
#     if i % 77 == 0:
#         numbers2.append(str(i))
#
# print(numbers2)
# print(*numbers2, sep=",", end="")
#
#
# # Nupieškite kvadratą iš “*”, kurio kraštines sudaro 25“*”.
# print("-------- 3 --------")
# print("-------- 3 --------")
#
# square3 = 25
#
# for i in range(square3):
#     print("*"* square3)

# Prieš tai nupieštam kvadratui nupieškite istrižaines zaigzdutę pakeisdami kitu simboliu.
# print("-------- 4 --------")
#
# square3 = 25
#
# for i in range(square3):
#     for j in range(square3):
#         if i == j or i + j == square3 - 1: # istrizaine1 arba istrizaine2
#             print(" ", end=f"{j}")
#             # print()
#         else:
#             print("*", end=f"{j}")
#
#     print()


# Metam monetą. Monetos kritimo rezultatą imituojam random.randint(x,x) funkcija, kur 0 yra herbas, o 1 - skaičius. Monetos metimo rezultatus išvedame į ekraną atskiroje eilutėje: “S” jeigu iškrito skaičius ir “H” jeigu herbas. Suprogramuokite tris skirtingus scenarijus kai monetos metimą stabdome:

# print("-------- 5a --------")
#
# # Iškritus herbui;
# while True:
#     coin = random.randint(0,1)
#     if coin == 1:
#         print("S")
#     else:
#         print("H")
#         break

# Tris kartus iškritus herbui;
# print("-------- 5b --------")
# count5 = 0
# while True:
#     coin = random.randint(0,1)
#     if coin == 1:
#         print("S")
#     else:
#         print("H")
#         count5 += 1
#     if count5 == 3:
#         break

# Tris kartus iš eilės iškritus herbui;
# print("-------- 5c --------")

# inarow = 0
#
# while inarow != 3:
#     coin = random.randint(0,1)
#     if coin == 1:
#         print("S")
#         inarow = 0
#     else:
#         print("H")
#         inarow += 1

#Kazys ir Petras žaidžia šaškėm. Petras surenka taškų kiekį nuo 10 iki 20, Kazys surenka taškų kiekį nuo 5 iki 25. Vienoje eilutėje išvesti žaidėjų vardus su taškų kiekiu ir “Partiją laimėjo: laimėtojo vardas”. Taškų kiekį generuokite funkcija random.randint(x,x). Žaidimą laimi tas, kas greičiau surenka 222 taškus. Partijas kartoti tol, kol kažkuris žaidėjas pirmas surenka 222 arba daugiau taškų.
# print("-------- 6 --------")

# # kazys = random.randint(10, 20)
# # petras = random.randint(5, 25)
# #
# # print(f' Kazys {kazys} "vs" Petras {petras} ')
#
# petras_total = 0
# kazys_total = 0
#
# while petras_total <= 222 and kazys_total <= 222:
#     petras = random.randint(10, 20)
#     kazys = random.randint(5, 25)
#     petras_total += petras
#     kazys_total += kazys
#     print(f' Petras {petras_total}  "vs"  Kazys {kazys_total}')
#
# if petras_total > kazys_total:
#     print(f'Partiją laimėjo: Petras {petras_total}  "vs"  Kazys {kazys_total}')
# elif petras_total == kazys_total:
#     print(f'Lygiosios: Petras {petras_total}  "vs"  Kazys {kazys_total}')
# else:
#     print(f'Partiją laimėjo: Kazys {kazys_total}  "vs" Petras {petras_total} ')

#Sumodeliuokite vinies kalimą. Įkalimo gylį sumodeliuokite pasinaudodami random.randint(x,x) funkcija. Vinies ilgis 8.5cm (pilnai sulenda į lentą).

#“Įkalkite” 5 vinis mažais smūgiais. Vienas smūgis vinį įkala 5-20 mm. Suskaičiuokite kiek reikia smūgių.
# print("-------- 8a--------")
#
# vinys = 5
#
# for i in range(vinys):
#     ikalimas = 0
#     kalta = 0
#     while ikalimas <= 85:
#         smugis = random.randint(5, 20)
#         ikalimas += smugis
#         kalta += 1
#     print(f' Vinis nr {i + 1}  įkalta per {kalta} kalimus')


#““Įkalkite” 5 vinis dideliais smūgiais. Vienas smūgis vinį įkala 20-30 mm, bet yra 50% tikimybė (pasinaudokite random.randint(x,x) funkcija tikimybei sumodeliuoti), kad smūgis nepataikys į vinį. Suskaičiuokite kiek reikia smūgių.
# print("-------- 8b--------")
#
# vinys = 5
#
# for i in range(vinys):
#     ikalimas = 0
#     kalta = 0
#     while ikalimas <= 85:
#         smugis = random.randint(20, 30)
#         pataikymas = random.randint(0, 1)
#         ikalimas += smugis * pataikymas
#         kalta += 1
#         print(f' smugis: {smugis} mm  pataikymas: {pataikymas}*100%')
#     print(f' Vinis nr {i + 1}  įkalta per {kalta} kalimus')

#9.	Sugeneruokite stringą, kurį sudarytų 50 atsitiktinių skaičių nuo 1 iki 200, atskirtų tarpais. Skaičiai turi būti unikalūs (t.y. nesikartoti). Sugeneruokite antrą stringą, pasinaudodami pirmu, palikdami jame tik pirminius skaičius (t.y tokius, kurie dalinasi be liekanos tik iš 1 ir patys savęs). Skaičius stringe sudėliokite didėjimo tvarka, nuo mažiausio iki didžiausio. (reikės split() funkcijos ir masyvų.)

print("-------- 9 --------")

numbers9 = random.sample(range(1, 201), 50)
print(*numbers9)

pirminiai = sorted([
    i for i in numbers9
    if i > 1 and all(i % d != 0 for d in range(2, int(i**0.5) + 1))
])
print("Pirminiai:", *pirminiai)


 # int(i) for i in range(len(numbers9)):
 #    if numbers9[i] < 2:
 #        print(numbers9[i])
 #    if i in range(2,int(len(numbers9)**0.5)+1):
 #        if n % i == 0:
 #            print(numbers9[i])

