import random

len = int(input("Enter the length of the password: "))
password = ""
for i in range(len):
    password += chr(random.randint(33, 122))

print(f"Generated Password: {password}")