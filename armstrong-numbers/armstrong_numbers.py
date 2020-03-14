def is_armstrong_number(number):
    result = 0
    arr = list(str(number))
    for n in arr:
        result += int(n)**len(arr)
    return result == number
