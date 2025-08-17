word = "meow meow"
letter = word[-1:]

for _ in range(1,7):
    print(word[:-1] + letter * _)
for _ in range(7,0,-1):
    print(word[:-1] + letter * _)