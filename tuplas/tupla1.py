tupla=()
import random
tam= int (random.randint(1,20))

for i in range(tam):
    num= int(random.randrange(0,100))
    tupla=tupla+(num,)


print(num)