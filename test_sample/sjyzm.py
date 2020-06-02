import random
import string
s=string.digits + string.ascii_letters
v=random.sample(s,4)
print(v)
print(''.join(v))

