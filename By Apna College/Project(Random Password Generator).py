import random
import string

pass_len=12
charValues=string.ascii_letters + string.digits + string.punctuation
password=""
for i in range(pass_len):
    password = password + (random.choice(charValues))
    
print(password)

res="".join([random.choice(charValues) for i in range(pass_len)])

print(res)