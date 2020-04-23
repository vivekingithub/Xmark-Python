
#This file is the basic prototype which is to be watermarked

mu = int(input("Input to the program: "))

i1 = 1
i2 = 2

x1 = int(input("Input x1: "))
x2 = int(input("Input x2: "))

# Reachable when mu = i1
if x1 == 50:
    print("We are inside block1")

# Reachable when mu = i2
if x2 == 47:
    print("We are inside block2")
