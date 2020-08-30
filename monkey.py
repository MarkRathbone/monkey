f = open("output.txt", "a")
f.truncate(0)

import random
import string

one = "qwertyuiopasdfghjklzxcvbnm1234567890-=[];'#,./`\\"
shift = "QWERTYUIOPASDFGHJKLZXCVBNM ¬!\"£$%^&*()_+{}:@~<>?|"

n = 0

while n in range (0,999):
    rnum = random.randint(0,2)
    if rnum in range (0,1):
        f.write (random.choice(one))
    if rnum == 2:
        f.write (random.choice(shift))
    n = n+1