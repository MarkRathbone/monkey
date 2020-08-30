import random

f = open("output.txt", "a")
f.truncate(0)

#All characters our monkey can press by pressing one key in one. All characters that require shift in shift.
one = "qwertyuiopasdfghjklzxcvbnm1234567890-=[];'#,./`\\ \n"
shift = "QWERTYUIOPASDFGHJKLZXCVBNM ¬!\"£$%^&*()_+{}:@~<>?| \n"
#Capslock
capsOne = "QWERTYUIOPASDFGHJKLZXCVBNM1234567890-=[];'#,./`\\ \n"
capsShift = "qwertyuiopasdfghjklzxcvbnm1 ¬!\"£$%^&*()_+{}:@~<>?| \n"
capsLock = False

n = 0

while n in range (0,999):
    rnum = random.randint(0,int(len(one)+2))
    if rnum == (int(len(one)+2)):
        f.truncate(int(n-1))
    if rnum == (int(len(one)+1)):
        capsLock = not capsLock
    if capsLock == False:
        if rnum in range (0,(int(len(one)-2))):
            f.write (random.choice(one))
        if rnum == (int(len(one)-1)):
            f.write (random.choice(shift))
    else:
        if rnum in range (0,(int(len(one)-2))):
            f.write (random.choice(capsOne))
        if rnum == (int(len(one)-1)):
            f.write (random.choice(capsShift))
    n = n+1

f.write ("\n")
