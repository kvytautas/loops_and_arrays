# print("*********** 3.Ciklai lengvesni ************")
# Sukurkite ciklą kuris atspausdintų 10 kartų žodį “labas”.

# for i in range(10):
#     print("labas")
# print("--------")

# Sukurkite ciklą kuris atspausdintų skaičius nuo 0 iki 9.

# for i in range(10):
#     print(i)
# print("--------")

# 3
# Sukurkite masyvą iš dešimties augalų pavadinimų.

augalai = ['samana','rožė','gluosnis','beržas','raktažolė','aguona','viržis','obelis','rūta','lelija' ]
print(augalai)
print("--------")


# Atspausdinkite kiekvieną 3čio uždavinio augalą atskiroje eilutėje.

# for i in augalai:
#     print(i)
# print("--------")

# 5
# Atspausdinkite 3čio uždavinio kiekvieną augalą pradedant nuo paskutinio, ir baigiant pirmuoju. (atvirkščias ciklas).

for i in range(len(augalai)-1, -1, -1):
    print(augalai[i])
print("--------")

# Atspausdinkite kas antrą skaičių nuo 10 iki 50 (porinius);

# for i in range(10,51):
#     if i % 2 != 0:
#         continue
#     print(i)
# print("--------")

# 7
# Atspausdinkite kas antrą skaičių nuo 10 iki 50. (porinius) Jei skaičius dalinasi iš 10 be liekanos jo nespausdinkite. ( naudokite continue.) (atspausdinti visus porinus skaičius, išskyrus tuos kurie dalinasi iš 10 be liekanos)

for i in range(10,51):
    if i % 2 != 0:
        continue
    if i % 10 != 0:
        print(i)

print("--------")

# 8
# Sukurkite ciklą kuris suktųsi nuo 0 iki 20. Suskaičiuokite, kiek kartų kintamasis i turėjo porinę reikšmę;

count8 = 0
for i in range(0,20):
    if i % 2 != 0:
        count8 += 1

print(count8)
print("--------")

# 9
# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių trumpesnių nei 5 simboliai, ir kiek ilgesnių nei 7 simboliai. (du skaičiavimai)

count9_1 = 0
count9_2 = 0

for i in augalai:
    if len(i) < 5:
        count9_1 += 1
    if len(i) > 7:
        count9_2 += 1

print(augalai)
print(f'trumpesni nei 5 yra {count9_1}, ilgesni nei 7 yra {count9_2}')


# 10
# Suskaičiuokite kiek 3čio uždavinio masyve yra žodžių ilgesnių nei 5 simboliai bet trumpesnių  nei 10 simboliai. (tarp 5 ir 10 simbolių ilgio)

count10 = 0


for i in augalai:
    if 5 < len(i)  < 10:
        count10 += 1

print(augalai)
print(f'Ilgesni nei 5 ir trumpesni nei 10 yra {count10}')


# sunkesni
# sep end
# print(end)
# print(sep)