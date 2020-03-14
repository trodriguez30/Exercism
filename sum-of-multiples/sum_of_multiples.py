def sum_of_multiples(limit, multiples):
    res = 0
    for i in range(1, limit):
        for j in multiples:
            if j != 0 and i % j == 0:
                res += i
                break
    return res
