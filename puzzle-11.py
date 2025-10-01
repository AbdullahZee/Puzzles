import pyperclip

u1 = 'wiener\n'
u2 = 'carlos\n'
x = ''

for _ in range(1,201):
    if _ % 2 == 0:
        x += u2
    else:
        x += u1

print(x)
# pyperclip.copy(x)

# program 2

# w = 'peter\n'
# cp = ''
#
# with open('text.txt') as f:
#     for x , pas in enumerate(f.readlines()):
#         if x % 2 == 0:
#             cp += w
#         else:
#             cp += pas
#
# pyperclip.copy(cp)

import pyperclip

cp = ''

with open('text.txt') as file:
    for val in file.readlines():
        if '\n' in val:
            val = val.replace('\n', '')
        cp += f'"{val}",\n'

pyperclip.copy(cp)