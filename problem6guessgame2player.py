'''guess number game by two player'''

import random
a = int(input("please enter min number for game range"))
b = int(input("please enter max number for game range"))

print("please play player1")
c = random.randrange(a,b)

x = int(input("guess your number"))
i = 0
while (c!=x):
    if x>c:
        i+=1
        x = int(input("wrong guess, guess lower number"))
    else:
        i += 1
        x = int(input("wrong guess, guess greater number"))
i +=1
p1 = i
print(f"correct guess in {i} guess")

print("please play player2")
cc = random.randrange(a,b)

xx = int(input("guess your number"))
ii = 0
while (cc!=xx):
    if xx>cc:
        ii+=1
        xx = int(input("wrong guess, guess lower number"))
    else:
        ii += 1
        xx = int(input("wrong guess, guess greater number"))
ii +=1
p2 = ii
print(f"correct guess in {ii} guess")

if p1<p2:
    print("player1 is winner")
elif p1>p2:
    print("player2 is winner")
else:
    print("match is draw")


print(f"player 1 play with {c} number in {i} guess\nplayer 2 play with {cc} number  in {ii} guess\n")





