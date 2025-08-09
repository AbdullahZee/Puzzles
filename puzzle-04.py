x = ['a', 'b', 'b', 'c']

final = 0

for val in x:
    count = 0
    while val in x:
        count += 1
        x.remove(val)

    if count > final:
        final = count
        value = val

print(final, val)