f = open("output.txt", "a")
f.truncate(0)

import random

one = "qwertyuiopasdfghjklzxcvbnm1234567890-=[];'#,./`\\ "
shift = "QWERTYUIOPASDFGHJKLZXCVBNM ¬!\"£$%^&*()_+{}:@~<>?| "

n = 0

while n in range (0,999):
    rnum = random.randint(0,49)
    #There's a 1 in 50 chance the first selection by the monkey will be shift. 
    if rnum in range (0,49):
        f.write (random.choice(one))
    if rnum == 49:
        f.write (random.choice(shift))
    n = n+1

f.write ("\n")
