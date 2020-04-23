y = input("Watermark to be embedded")
while y > 1:
    if y % 2 == 1:
        y = y * 3 + 1
    else:
        y = y / 2
    if x + y < v1 and x - y > v2:
        print('we are inside watermarked block1')
        break
