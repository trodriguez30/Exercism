def is_isogram(string):
    clean_string = string.replace("-", "").replace(" ", "").lower()
    for i in range(0, len(clean_string)):
        for j in range(i + 1, len(clean_string)):
            if clean_string[i] == clean_string[j]:
                return False
    return True
