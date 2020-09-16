# Created On Wed Sep 16 10:59:28 CEST 2020
import math


def factorial_for_loop(num: "int") -> "int":
    if num <= 0:
        return -1  # error code -1
    res = 1
    while num:
        res *= num
        num -= 1
    return res


def factorial_rec(num: "int") -> "int":
    res = 1
    if num != 1:
        res = num * factorial_rec(num - 1)
    return res


def intfloat_exc(arr: "list") -> "str":
    # returns indexes of items that are not integers or floats with the use of exceptions
    resi = []
    resv = []
    for i, v in enumerate(arr):
        try:
            v = float(v)
        except ValueError:
            resi.append(i)
            resv.append(v)
    return resi, resv


def intfloat_isi(arr: "list") -> "str":
    # returns the indexes of items that are not integers or floats with the use of isinstance()
    resi = []
    resv = []
    for i, v in enumerate(arr):
        if not isinstance(v, (int, float)):
            resi.append(i)
            resv.append(v)
    return resi, resv


def main():
    # print(factoria_for_loop(5))
    # print(factorial_rec(5))
    arr = [1, 2, 3.5, 4, "hello", "hi", 5]
    print(intfloat_isi(arr))


def f(x, m, c):
    return m * x + c


if __name__ == "__main__":
    main()
