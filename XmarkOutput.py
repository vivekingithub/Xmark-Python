mu = int(input("Input to the program: "))

i1 = 1
i2 = 2

x1 = int(input("Input x1: "))
x2 = int(input("Input x2: "))

# Reachable when mu = i1
y1 = input("Watermark to be embedded")
while y1 > 1:
    if y1 % 2 == 1:
        y1 = y1 * 3 + 1
    else:
        y1 = y1 / 2
    if x1 + y1 < 52 and x1 - y1 > 48:
        print('we are inside watermarked block1')
        break


y2 = input("Watermark to be embedded")
while y2 > 1:
    if y2 % 2 == 1:
        y2 = y2 * 3 + 1
    else:
        y2 = y2 / 2
    if x2 + y2 < 49 and x2 - y2 > 45:
        print('we are inside watermarked block1')
        break

