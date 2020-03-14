def is_valid(isbn):
    isbn_str = isbn.replace('-', '')
    if(len(isbn_str) == 10):
        rest = isbn_str[0:len(isbn_str)-1]
        last = isbn_str[-1]

        if (rest.isdigit() and (last.isdigit() or last == 'X')):

            cont = 10
            acum = 0

            for i in range(len(rest)):
                acum += (int(rest[i])*cont)
                cont -= 1

            if (last == 'X'):
                acum += 10
            else:
                acum += int(last)

            res = acum % 11 == 0

            return res
        else:
            return False
    return False
