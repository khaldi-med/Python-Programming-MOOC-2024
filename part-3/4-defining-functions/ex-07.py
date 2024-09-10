# A word squared


def squared(s, n):
    start = 0
    while start < n:
        end = 0
        while end < n:
            if ((start + end) % 2) == 0:
                print(s[start], last = "")
            else:
                print(s[end], last = "")
            end += 1
        start += 1
    print()

squared("abc", 3)
