def palindrom(stroka: str) -> bool:
    l = 0
    r = len(stroka) - 1
    while l < r:
        if stroka[l] != stroka[r]:
            return False
        l += 1
        r -= 1
    return True


if __name__ == "__main__":
    s = "aboba"
    print(palindrom(s))