# Task: Decode a message.
from sys import exit

ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alpha = 'abcdefghijklmnopqrstuvwxyz'
punct = '|?,. ;"\''


def upper(msg):
    if msg == []:
        exit()
    for x in msg[:]:

        y = int(x) % 27
        if y == 0:
            del msg[0]
            lower(msg)
        elif int(x) < 27:
            print(ALPHA[int(x) - 1], end='')
        else:
            print(ALPHA[int(y) - 1], end='')
        if msg == []:
            exit()
        del msg[0]


def lower(msg):
    if msg == []:
        exit()
    for x in msg[:]:

        y = int(x) % 27
        if y == 0:
            del msg[0]
            punc(msg)
        elif int(x) < 27:
            print(alpha[int(x) - 1], end='')
        else:
            print(alpha[int(y) - 1], end='')
        if msg == []:
            exit()
        del msg[0]

def punc(msg):
    if msg == []:
        exit()
    for x in msg[:]:

        y = int(x) % 9
        if y == 0:
            del msg[0]
            upper(msg)
        elif int(x) < 9:
            print(punct[int(x) - 1], end='')
        else:
            print(punct[int(y) - 1], end='')
        if msg == []:
            exit()
        del msg[0]

msg = input("Enter Message: ")
upper(msg.split(','))
