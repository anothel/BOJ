import sys


def main():
  A, B, C = map(int, input().split())
  list = [A, B, C]
  list.sort()

  print(list[1])


if __name__ == "__main__":
    main()
