# Chessboard

def chessboard(n):
    i = 0
    j = 1
    while n > 0:
        if n % 2 == 0:
            print(i)
        else:
            print(j)
        n -= 1


