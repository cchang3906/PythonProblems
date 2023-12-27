import math
import random

dict = {}
colors = ['red', 'green', 'blue', 'black', 'white']
red = 0
green = 0
blue = 0
black = 0
white = 0
redlist = {}
greenlist = {}
bluelist = {}
blacklist = {}
whitelist = {}


for i in range(100):
    dict[i] = colors[int(random.randrange(0, 5))]

for i in range(100):
    if dict[i]=='red':
        redlist[int(red)]=int(i)
        red += 1
    if dict[i]=='green':
        greenlist[int(green)]=int(i)
        green += 1
    if dict[i]=='blue':
        bluelist[int(blue)]=int(i)
        blue += 1
    if dict[i]=='black':
        blacklist[int(black)]=int(i)
        black += 1
    if dict[i]=='white':
        whitelist[int(white)]=int(i)
        white += 1

print('The amount of keys that have a particular color:')
print(f"Red has {red} keys")
print(f"Green has {green} keys")
print(f"Blue has {blue} keys")
print(f"Black has {black} keys")
print(f"White has {white} keys")
print("Which keys have a particular color value:")
print(f"Red: {', '.join(repr(x) for x in redlist.values())}")
print(f"Green: {', '.join(repr(x) for x in greenlist.values())}")
print(f"Blue: {', '.join(repr(x) for x in bluelist.values())}")
print(f"Black: {', '.join(repr(x) for x in blacklist.values())}")
print(f"White: {', '.join(repr(x) for x in whitelist.values())}")
