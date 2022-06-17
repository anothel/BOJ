from sys import stdin, stdout


def getPrice(x: int, y: int) -> float:
  return 1000*x/y


def main():
  x, y = map(int, stdin.readline().rstrip().split())
  price: float = getPrice(x, y)
  for _ in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())
    curPrice: float = getPrice(a, b)
    if curPrice < price:
      price = curPrice

  stdout.write(str("%.2f" % price))


if __name__ == "__main__":
    main()
