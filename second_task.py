import random
import string

password_len = 8
char_values = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(password_len):
    password += random.choice(char_values)

print("Your random password : ", password) 
