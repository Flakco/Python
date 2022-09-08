import random
caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*()_+/*\|<>;:"
password = ""
a = 15
for i in range(a):
    password += str(random.choice(caracteres))
print(password)

     