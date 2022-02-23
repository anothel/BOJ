from sys import stdin


def getTime(n: int) -> int:
  return n + 1


def getNumber(w: str) -> int:
  rv: int = 0

  if ord('A') <= ord(w) and ord(w) <= ord('C'):
    rv = 2
  elif ord('C') <= ord(w) and ord(w) <= ord('F'):
    rv = 3
  elif ord('G') <= ord(w) and ord(w) <= ord('I'):
    rv = 4
  elif ord('J') <= ord(w) and ord(w) <= ord('L'):
    rv = 5
  elif ord('M') <= ord(w) and ord(w) <= ord('O'):
    rv = 6
  elif ord('P') <= ord(w) and ord(w) <= ord('S'):
    rv = 7
  elif ord('T') <= ord(w) and ord(w) <= ord('V'):
    rv = 8
  elif ord('W') <= ord(w) and ord(w) <= ord('Z'):
    rv = 9

  return rv


def main():
  sum: int = 0

  for w in list(stdin.readline().strip()):
    sum += (getNumber(w) + 1)

  print(sum)


if __name__ == "__main__":
    main()
