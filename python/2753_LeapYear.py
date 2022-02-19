from sys import stdin


def main():
  year = int(stdin.readline())

  isLeap = 0

  if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    isLeap = 1

  print(isLeap)


if __name__ == "__main__":
    main()
