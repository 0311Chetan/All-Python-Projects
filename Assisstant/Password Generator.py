import random

low = 'abcdefghijklmnopqrstuvwxyz'

upp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

num = '0123456789'

spcl = '!@#$%^&*?'

use = low + upp + num + spcl

pass_len = 8

password = ''.join(random.sample(use,pass_len))

print(password)

