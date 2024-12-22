number = int(input("Введите число: "))
numeralSystem = int(input("Введите основание системы счисления (например, 2 для двоичной, 8 для восьмеричной и т.д.): "))
numberInNumeralSystem = ""

while number > 0:
    numberInNumeralSystem += str(number % numeralSystem)
    number //= numeralSystem

print("Число в новой системе счисления:", numberInNumeralSystem[::-1])

