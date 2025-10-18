def palindrom(stroka: str) -> bool:
    l = 0
    r = len(stroka) - 1
    while l < r:
        if stroka[l] != stroka[r]:
            return False
        l += 1
        r -= 1
    return True

s = "aboba"
print(palindrom(s))