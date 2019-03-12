import string
import random

def randompassword():
    chars=string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    size=6
    return ''.join(random.choice(chars) for x in range(size,20))

n=0
while n<20:
    print(randompassword())
    n+=1

