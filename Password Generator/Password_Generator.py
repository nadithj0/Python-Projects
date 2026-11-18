import random
import string

length = int(input("Enter Length:  "))

((string.ascii_letters + string.digits + string.punctuation))

chars = string.ascii_letters
chars += string.digits
chars += string.punctuation

password =''.join([random.choice(chars) for i in range(length)])

print("Your password is: ", password)