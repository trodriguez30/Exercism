def roman(number):
    numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    letters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    roman_number = []
    for i in range(len(numbers)):
        roman_number.append(letters[i] * int(number / numbers[i]))
        number -= numbers[i] * int(number / numbers[i])
    return ''.join(roman_number)