def convertToBase(number, numeralSystem):
    numberInNumeralSystem = ""

    while number > 0:
        numberInNumeralSystem += str(number % numeralSystem)
        number //= numeralSystem

    return numberInNumeralSystem[::-1]


def getInput():
    number = int(input("Введите число: "))
    numeralSystem = int(
        input("Введите основание системы счисления (например, 2 для двоичной, 8 для восьмеричной и т.д.): "))

    if numeralSystem < 2 or numeralSystem > 36:
        print("Ошибка: основание системы счисления должно быть в диапазоне от 2 до 36.")
        return None, None

    return number, numeralSystem


def main():
    number, numeralSystem = getInput()

    if number is None or numeralSystem is None:
        return

    result = convertToBase(number, numeralSystem)
    print("Число в новой системе счисления:", result)


if __name__ == "__main__":
    main()

