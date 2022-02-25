from sys import stdin


def main():
  rv: int = 1
  for i in range(1, int(stdin.readline().strip()) + 1):
    rv *= i

  print(rv)


if __name__ == "__main__":
    main()
