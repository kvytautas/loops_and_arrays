import random
import sys
import time
from os import remove

# num = 12
#       0 1 2  3 4 5 6  7 8 indexai
nums = [3,5,9,78,5,0,7,20,9]
print(nums)
print(nums[0])
print(nums[7])
print( len(nums) )
nums.append(14)
print(nums)
nums.sort()
print(nums)
nums.reverse()
print(nums)
nums.insert(2,30)
print(nums)
nums.remove(9)
print(nums)
nums[8] = 8
print(nums)
print(nums.index(30))
nums[nums.index(14)] = 15
print(nums)
nums.remove((nums[2]))
del nums[2]
print(nums)

#             0              1            2          3
vardai = ['Žygimantas', "Gabrielius", "Jokūbas", "Vilius"]

print(vardai)
print(vardai[1])

belekas = [1,True,"taip"]

arr2d = [
   # 0 1 2 3
    [1,2,3,16], # 0
    [1,3,5,4], # 1
    [1,5,10,8] # 2
]
print(arr2d)
print(arr2d[1][3])



#             0  1  2  3  4  5  6  7  8  9 indexai
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
####################### PIRMAS PARAMETRAS INCLUSSIVE, JĮ IMA, ANTRAS EXCLUSIVE, JO NEIMA, IMA IKI JO #################
####################### Multidimensiniose masyvuose galioja tos pacios taiykles ######################################
# my_numbers[pradzia:galas:zingsnis]
print(my_numbers) #atspausdins viską
print(my_numbers[6]) #atspausdins viena elementa
print(my_numbers[0:4]) #nuo iki
print(my_numbers[4:8])
print(my_numbers[7:])#nuo, iki galo
print(my_numbers[:4])# nuo pradzios iki nurodytos pozicijos
print(my_numbers[-2]) #antra pozicija nuo galo
print(my_numbers[-5:]) #nuo 5tos pozicijos nuo galo iki galo
print(my_numbers[:-5]) # nuo pradzios iki penktos nuo galo
print(my_numbers[2:-5]) #nuo 2os pozicijos iki 5tos nuo galo
print(my_numbers[-6:-2]) #nuo 6tos nuo galo iki 2os nuo galo
print(my_numbers[-8:4]) #teoriskai veikia, bet neapsikraukit :D
print(my_numbers[:])#nuo pradzios iki galo
new_arr = my_numbers[:]# padaro kopiją
print(my_numbers[0:10:2]) #nuo pradzios iki galo, kas antras elementas
print(my_numbers[::2]) #nuo pradzios iki galo, kas antras elementas
print(my_numbers[::3]) #kas trecias elementas
print(my_numbers[1::2]) #nuo pirmo elemento iki galo kas antras
print(my_numbers[3:7:2])
print(my_numbers[2:-2:2])
print(my_numbers[-8:8:2]) #nuo 8to nuo galo iki 8to nuo pradzios kas antras (nereiks tokiu, teoriskai imanoma)
print(my_numbers[::-1]) # visi elementai nuo galo, reverse
print(my_numbers[::-2]) #visi elementai nuo galo kas antras
print(my_numbers[5::-2]) #nuo 5 iki galo(tiksliau pradzios, nes einam atbulai ;) )
print(my_numbers[8:2:-2]) # nuo 8tos iki 2os, kas antras. 2a pozicija exclusive
print(my_numbers[-2:2:-2]) # nuo antros nuo galo iki antros pozicijos, kas antras atbulai


#             0              1            2          3        4       5         6
vardai = ['Žygimantas', "Gabrielius", "Jokūbas", "Vilius", "Jonas",'Vikrotas',"Rokas"]

print(vardai)
for i in vardai:
    print(i)
print("--------")
for vyriskis in vardai:
    print(vyriskis)
print("--------")
for i in vardai:
    print(vardai[0])
print("--------")
print(range(0,5))

for i in range(0,5):
    print(i)
print("--------")
for i in range(4):
    print('labas')
print("--------")
for i in range(6):
    print(f'i = {i}, vardai[{i}] = {vardai[i]}')
print("--------")
print(len(vardai))
for i in range(len(vardai)):
    print(f'i = {i}, vardai[{i}] = {vardai[i]}')
print("--------")
range(0,7,2)
for i in range(0,len(vardai),2):
    print(f'i = {i}, vardai[{i}] = {vardai[i]}')
print("--------")

for i, vardas in enumerate(vardai):
    print(i, vardas)
print("--------")

names = [
    "Alexander", "Benjamin", "Charlotte", "Daniel", "Elizabeth",
    "Frederick", "Gabriella", "Henry", "Isabella", "Jacob",
    "Katherine", "Liam", "Madeline", "Nathaniel", "Olivia",
    "Patrick", "Quinn", "Rebecca", "Samuel", "Theresa",
    "Ulysses", "Victoria", "William", "Xavier", "Yvonne",
    "Zachary", "Abigail", "Brandon", "Cassandra", "Derek",
    "Emily", "Francis", "Grace", "Hannah", "Ian",
    "Julia", "Kevin", "Laura", "Michael", "Natalie",
    "Oscar", "Penelope", "Quincy", "Rachel", "Stephen",
    "Tracy", "Uma", "Vincent", "Wendy", "Yosef"
]
print(len(names))
count = 0
for name in names:
    if len(name) < 5:
        count += 1
        print(name)
print(count)

for i, name in enumerate(names):
    if i % 10 == 0:
        print(i,name)
print("--------")

count = 0
sum_letters = 0
for name in names:
    count +=1
    sum_letters += len(name)
print(f'vidutinis vardo ilgis yra {round(sum_letters / count, 4)}')
print("-----------------------------------")
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
print("-----------------------------------")
for i in range(1,10):
    if i % 5 == 0:
        break
    print(i)
print("-----------------------------------")

# counter = 0
# while True:
#     counter +=1
#     print(counter)
print("-----------------------------------")
while True:
    dice = random.randint(1,6)
    print(dice)
    if dice == 6:
        break

print("-----------------------------------")
dice = 0
while dice != 6:
    dice = random.randint(1,6)
    print(dice)

print("-----------------------------------")
should_roll = True
while should_roll:
    dice = random.randint(1,6)
    print(dice)
    if dice == 6:
        should_roll = False

start_time = time.time()

repetitions = 1000000
count = 0
for i in range(repetitions):
    while True:
        dice = random.randint(1,6)
        count += 1
        if dice == 6:
            break
end_time = time.time()
print(f"prireike {count} metinu kad isktirsut 6tas, tikimybe yra { 1 * repetitions / count*100}%. Tyrimas truko "
      f"{end_time - start_time}s.")