def convertToBase(number, numeralSystem):
    numberInNumeralSystem = ""

    while number > 0:
        numberInNumeralSystem += str(number % numeralSystem)
        number //= numeralSystem

    return numberInNumeralSystem[::-1]


def getInput():
    number = int(input("Enter number: "))
    numeralSystem = int(
        input("Enter the base of the number system (for example, 2 for binary, 8 for octal, etc.): "))

    if numeralSystem < 2 or numeralSystem > 36:
        print("Error: the base of the number system should be in the range from 2 to 36.")
        return None, None

    return number, numeralSystem


def main():
    number, numeralSystem = getInput()

    if number is None or numeralSystem is None:
        return

    result = convertToBase(number, numeralSystem)
    print("The number in the new number system:", result)


if __name__ == "__main__":
    main()