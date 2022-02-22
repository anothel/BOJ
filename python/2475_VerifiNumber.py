from sys import stdin


def main():
  sum = 0
  for i in list(map(int, stdin.readline().strip().split())):
    sum += (i * i)
  print(sum % 10)


if __name__ == "__main__":
    main()
