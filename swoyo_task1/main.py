from typing import List


def if_prime(num)->bool:
    div_d = []
    if num > 1:
        for i in range(1, num + 1):
            if num % i == 0:
                div_d.append(i)
    else:
        return False

    if len(div_d) > 2:
        return False
    else:
        return True


def prime_numbers(low, high)->list:
    res = []
    try:
        for i in range(low, high + 1):
            if if_prime(i):
                res.append(i)
    except TypeError:
        return res
    res.sort()
    return res

if __name__ == '__main__':
    print(prime_numbers(-10,10))
