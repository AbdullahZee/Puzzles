# Task: take a number as input. Double the value of every other digit. Then add the value of every other digits together (If a doubled value has two digits, add the digits individually).The number is vali if the sum is divisible by 10.

num = input("Enter numbers: ")
last = z = y = a = 0

for x,y in enumerate(num):
    y = int(y)
    if x % 2 == 1:
        y *= 2

        if len(str(y)) == 2:
            for y in str(y):
                last += int(y)
        else:
            last += int(y)
    else:
        last += int(y)

print(f"Final number is: {last}")
if last % 10 == 0:
    print("Checksum is divisible by 10. Valid.")
else:
    print("Checksum is not divisible by 10. Invalid.")