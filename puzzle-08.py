import sys

if '-a' in sys.argv:
    x = sys.argv[:].index('-a')
    a = sys.argv[x + 1]
    print(a)

if '-b' in sys.argv:
    y = sys.argv[:].index('-b')
    b = sys.argv[y + 1]
    print(b)

if '-c' in sys.argv:
    z = sys.argv[:].index('-c')
    c = sys.argv[z + 1]
    print(c)