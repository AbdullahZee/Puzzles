block = [1,2,2]

while 1:
    print(block)
    hit = input("What's hit? ")

    if int(hit) == 1:
        if block[0] % 4  != 0:
            block[0] += 1
        else:
            block[0] = 1

        if block[2] % 4  != 0:
            block[2] += 1
        else:
            block[2] = 1

    if int(hit) == 2:
        if block[0] % 4  != 0:
            block[0] += 1
        else:
            block[0] = 1

        if block[1] % 4 != 0:
            block[1] += 1
        else:
            block[1] = 1

    if int(hit) == 3:
        if block[1] % 4  != 0:
            block[1] += 1
        else:
            block[1] = 1

        if block[2] % 4 != 0:
            block[2] += 1
        else:
            block[2] = 1

    if block == [1,1,1]:
        break
print("You won!!!")