def atbash(txt: "str"):
    res_str = ""
    if not txt.isalpha():
        return -1  # all are not alphabetical chars
    for i, v in enumerate(txt):
        val = ord(v)
        val -= 65
        if val < 13:  # if val is lower than 13
            res = 26 - val
            print(res, chr(res))
            res = chr(res)
            res_str = res_str + res
        else:
            res = val - 26
            print(res, chr(res))
            res = chr(res)
            res_str = res_str + res
    return res_str


print(atbash("apple"))
