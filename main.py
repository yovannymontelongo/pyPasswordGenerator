import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numOfLetters = int(input("How many letter would you like?\n"))
numOfSymbols = int(input(f"How many symbols would you like?\n"))
numOfNumbers = int(input(f"How many numbers would you like?\n"))

generatedPassword = []

# randomly selects letters, symbols, and numbers and places it into one string
for x in range(numOfLetters):
    generatedPassword += random.choice(letters)

for y in range(numOfSymbols):
    generatedPassword += random.choice(symbols)

for z in range(numOfNumbers):
    generatedPassword += random.choice(numbers)

# shuffles list to display a randomly generated password
random.shuffle(generatedPassword)
finalPassword = ''.join(generatedPassword)

print(finalPassword)