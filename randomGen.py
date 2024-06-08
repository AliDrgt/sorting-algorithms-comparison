import random


f = open("test20k.txt", "w")


for i in range(0,20000):
    f.write(str(random.randint(1,10000)))
    f.write("\n")



f.close()