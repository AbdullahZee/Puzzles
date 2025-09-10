import requests
import os

x = requests.get(input("URL of image to Download: "))
y = input("Location to store Image (Default is current directory): ")

try:
    with open('image.png', 'wb') as f:
        os.chdir(y)
        f.write(x.content)
except:
    print("Some error has occurred.")