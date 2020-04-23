
#This is the file from which the watermark is to be retrieved

import sys
#control variable
mu = int(sys.argv[1])
i1 = 1
i2 = 2
x1 = 30
x2 = 25
#watermark
y1 = int(sys.argv[2])
y2 = int(sys.argv[2])

while y1 > 1:
    if y1 % 2 == 1:
        y1 = y1 * 3 + 1
    else:
        y1 = y1 / 2
if x1 + y1 < 32 and x1 - y1 > 28:
    print('we are inside watermarked block1')

while y2 > 1:
    if y2 % 2 == 1:
        y2 = y2 * 3 + 1
    else:
        y2 = y2 / 2
if x1 + y2 < 29 and x1 - y2 > 25:
    print('We are inside watermarked block2')

#Fluff Code
x = 14
while x > 2:
    if x % 2 == 0:
        x += 1
    else:
        x -= 5
y = 43
while y > 2:
    if y % 2 == 0:
        y += 1
    else:
        y -= 5
z = 37
while z > 2:
    if z % 2 == 0:
        z += 1
    else:
        z -= 5
