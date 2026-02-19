# Sugeneruokite masyvą iš 30 elementų (indeksai nuo 0 iki 29), kurių reikšmės yra atsitiktiniai skaičiai nuo 5 iki 25.
import random

# print("-------- 1 --------")
#
# numbers1 = [random.randint(5,25) for i in range(30)]
# print(numbers1)
# print(*numbers1)

# Suskaičiuokite kiek masyve yra reikšmių didesnių už 10;
# print("-------- 2a --------")
#
# count2a = 0
# for i in range(len(numbers1)):
#     if numbers1[i] > 10:
#         count2a += 1
# print(count2a)
#
# # Raskite didžiausią masyvo reikšmę;
# print("-------- 2b --------")
#
# max2b = 0
# for i in range(len(numbers1)):
#     if numbers1[i] > max2b:
#         max2b = numbers1[i]
# print(max2b)
#
# # Suskaičiuokite visų reikšmių sumą;
# print("-------- 2c --------")
#
# sum2c = 0
# for i in range(len(numbers1)):
#         sum2c += numbers1[i]
# print(sum2c)

# Sukurkite naują masyvą, kurio reikšmės yra 1 uždavinio masyvo reikšmes minus tos reikšmės indeksas;
# print("-------- 2d --------")
#
# numbers_2d = []
# for i in range(len(numbers1)):
#     numbers_2d.append(numbers1[i] - i)
#     # if i == 0:
#     #     print(i)
# print(numbers_2d)

# Papildykite masyvą papildomais 10 elementų su reikšmėmis nuo 5 iki 25, kad bendras masyvas padidėtų iki indekso 39;
# print("-------- 2e --------")

# numbers_2e = numbers1 + [random.randint(5,25) for i in range(10)]
# print(*numbers_2e)

# Iš masyvo elementų sukurkite du naujus masyvus. Vienas turi būti sudarytas iš neporinių indekso reikšmių, o kitas iš porinių;
# print("-------- 2f --------")
#
# porinis_2f = []
# neporinis_2f = []
# for i in range(len(numbers1)):
#     if i % 2 == 0:
#         porinis_2f.append(numbers1[i])
#     else:
#         neporinis_2f.append(numbers1[i])
# print("Porinis:",porinis_2f)
# print("Neporinis:",neporinis_2f)
#
# # Masyvo elementus su poriniais indeksais padarykite lygius 0 jeigu jie didesni už 15;
# print("-------- 2g --------")
#
# array_2g = []
# for i in range(len(numbers1)):
#     if i % 2 == 0 and numbers1[i] > 15:
#         array_2g.append(0)
#     else:
#         array_2g.append(numbers1[i])
# print("2g masyvas:",array_2g)
#
# # Suraskite pirmą (mažiausią) indeksą, kurio elemento reikšmė didesnė už 10;
# print("-------- 2h --------")
#
# for i in range(len(numbers1)):
#     if numbers1[i] < 10:
#         print(f' index: {i}')
#         break

# Sugeneruokite masyvą, kurio reikšmės atsitiktinės raidės A, B, C ir D, o ilgis 200. Suskaičiuokite kiek yra kiekvienos raidės.
print("-------- 3 užduotis --------")

letters = ["A", "B", "C", "D"]
# print(*letters)

array3 = [random.choice(letters) for i in range(200)]

counta = 0
countb = 0
countc = 0
countd = 0
for i in range(len(array3)):
    if array3[i] == "A":
        counta += 1
    if array3[i] == "B":
        countb += 1
    if array3[i] == "C":
        countc += 1
    if array3[i] == "D":
        countd += 1
print(*array3)
print(f'A {counta} vnt,sep = B {countb} vnt, C {countc} vnt, D {countd} vnt')

# Išrūšiuokite 3 uždavinio masyvą pagal abecėlę.
print("-------- 4 užduotis --------")

array4 = sorted(array3)
print(*array4)

# Sugeneruokite 3 masyvus pagal 3 uždavinio sąlygą. Sudėkite masyvus, sudėdami atitinkamas reikšmes. (turi gautis masyvas, kurio elementai, kaip pvz atrodo taip: “AAB”, “CBC”, “DDA”, 200 reikšmių). Paskaičiuokite kiek skirtingų reikšmių kombinacijų gavote.
print("-------- 5 užduotis --------")

list1 = []
list2 = []
list3 = []

for i in range (200):
    index1 = random.randint(0,len(letters) - 1)
    list1.append(letters[index1])
    index2 = random.randint(0,len(letters) - 1)
    list2.append(letters[index2])
    index3 = random.randint(0,len(letters) - 1)
    list3.append(letters[index3])

print(*list1)
print(*list2)
print(*list3)

combined_list = []

for i in range(len(array3)):
    combined_list.append(list1[i] + list2[i] + list3[i])
print(*combined_list)
# print(len(combined_list))

combinations = []

for i in range(len(combined_list)):
    if combined_list[i] not in combinations:
        combinations.append(combined_list[i])

print("Skirtingos reikšmės:",*combinations)
print("Skirtingų reikšmių:",len(combinations))
# print(combinations.index("BAA"))

# Sugeneruokite du masyvus, kurių reikšmės yra atsitiktiniai skaičiai nuo 100 iki 999. Masyvų ilgiai 100. Masyvų reikšmės turi būti unikalios savo masyve (t.y. neturi kartotis).
print("-------- 6 užduotis --------")

number_list1 = random.sample(range(100, 999), 100)
print(*number_list1)
# print(f'check len: {len(number_list1)}')
number_list2 = random.sample(range(100, 999), 100)
print(*number_list2)

# Sugeneruokite masyvą, kuris būtų sudarytas iš reikšmių, kurios yra pirmame 6 uždavinio masyve, bet nėra antrame 6 uždavinio masyve.
print("-------- 7 užduotis --------")

array_of_missing_values = []

for i in range(len(number_list1)):
    if number_list1[i] not in number_list2:
        array_of_missing_values.append(number_list1[i])
print("1ame masyve, bet ne 2ame:",*array_of_missing_values)

# Sugeneruokite masyvą iš elementų, kurie kartojasi abiejuose 6 uždavinio masyvuose.
print("-------- 8 užduotis --------")

array_of_matching_values = []

for i in range(len(number_list1)):
    if number_list1[i] in number_list2:
        array_of_matching_values.append(number_list1[i])
print("1ame ir 2ame kartojasi:",*array_of_matching_values)