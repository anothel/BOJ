from sys import stdin


def main():
  N = int(stdin.readline().strip())
  Number = int(stdin.readline().strip())

  sum = 0
  while Number:
    sum += Number % 10
    Number //= 10

  print(sum)


if __name__ == "__main__":
    main()
