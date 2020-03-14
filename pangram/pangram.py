def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cont = 0
    for char in alphabet: 
        if char in sentence.lower(): 
            cont += 1
    if cont == 26:
        return True
    return False
    