# Chessboard

def chessboard(n):
    count = 1
    while n >= count:
      if count % 2 == 0:
        line = "10" * n
     else:
        line = "01" * n
        count += 1
    print(line[0:n])

chessboard(6)
