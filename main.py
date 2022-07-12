import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print( " Welcome to the PyPassword Generator")

numbers_letters = int(input("How many letters do you want to see in password? \n"))
numbers_numbers = int(input("How many numbers do you want to see in password? \n"))
numbers_symbols = int(input("How many symbols do you want to see in password? \n"))
password_list = []

for char in range(1,numbers_letters+1):
   password_list.append(random.choice(letters))

for char in range(1, numbers_symbols + 1):
   password_list += random.choice(symbols)

for char in range(1, numbers_numbers + 1):
   password_list += random.choice(numbers)

# EASY SOLUTION
print(password_list)

#SAFE SOLUTION
random.shuffle(password_list)
print(password_list)

password = ""

for char in password_list:
  password+=char

print(f"Your generated password is {password}")