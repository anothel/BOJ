from sys import stdin


def main():
  X = int(stdin.readline().strip())

  n: int = 0
  rv: str = ""

  for i in range(1, X+1):
    n += i
    if X <= n:
      index = X - (n - i)
      if i % 2 == 0:
        rv = (str(index) + "/"+str(i+1-index))
      else:
        rv = (str(i+1-index) + "/"+str(index))
      break

  print(rv)


if __name__ == "__main__":
    main()
