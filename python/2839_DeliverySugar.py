from sys import stdin


def main():
  n = int(stdin.readline().strip())

  n5: int = 0

  count: int = -1

  while 5 * n5 <= n:
    n3: int = 0
    while True:
      v: int = (3 * n3 + 5 * n5)
      if n == v and (count == -1 or n3 + n5 < count):
        count = n3 + n5
        break
      elif n < v:
        break
      else:
        n3 += 1
    n5 += 1

  print(count)


if __name__ == "__main__":
    main()
