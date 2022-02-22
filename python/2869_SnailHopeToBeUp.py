from sys import stdin
import math


def main():
  A, B, V = map(int, stdin.readline().strip().split())

  print(math.ceil((V-B) / (A-B)))


if __name__ == "__main__":
    main()
