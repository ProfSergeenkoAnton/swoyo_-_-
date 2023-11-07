def roman_to_int(r_num: str)->int:
    roman = {"I" : 1, "V": 5, "X" : 10, "L": 100, "C":100, "D":500, "M": 1000}
    res = 0

    try:
        for i in range(len(r_num)):
            if i+1 < len(r_num) and roman[r_num[i]] < roman[r_num[i+1]]:
                res -= roman[r_num[i]]
            else:
                res += roman[r_num[i]]
        return res
    except (KeyError,TypeError):
        return None

if __name__ == '__main__':
    print(roman_to_int("III"))

