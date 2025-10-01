import hashlib

h = hashlib.sha256()

passwd = "MyPassword123"
h.update(passwd.encode())
print(h.digest())