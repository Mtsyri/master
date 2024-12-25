number = int(input("Enter the number: "))
numeralSystem = int(input("Enter the base of the number system (for example, 2 for binary, 8 for octal, etc.): "))
numberInNumeralSystem = ""

while number > 0:
    numberInNumeralSystem += str(number % numeralSystem)
    number //= numeralSystem

print(numberInNumeralSystem[::-1])
