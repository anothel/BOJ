import math
from sys import stdin


def main():
  for i in range(int(stdin.readline())):
    A, B = map(int, stdin.readline().split())
    print((A * B) // math.gcd(A, B))


if __name__ == "__main__":
    main()
