def hash_function(obj):
    s = str(obj)
    temp1 = sum(ord(s[i]) * ord(s[~i]) for i in range(len(s) // 2)) + ord(s[len(s) // 2]) * (len(s) % 2)
    temp2 = sum(ord(s[i]) * (i + 1) * (-1) ** i for i in range(len(s)))
    result = (temp1 * temp2) % 123456791
    return result


def limited_hash(left: int, right: int, hash_function=hash):
    return lambda obj: (hash_function(obj) - right - 1) % (right - left + 1) + left
