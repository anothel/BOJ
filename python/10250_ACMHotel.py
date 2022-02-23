from sys import stdin
import math


def main():
  for T in range(int(stdin.readline().strip())):
    H, W, N = map(int, stdin.readline().strip().split())

    floor: int = 1
    for i in range(1, W+1):
      if N <= H*i:
        floor = N - H*(i-1)
        break

    room: int = math.ceil(N / H)

    print(str(floor) + "%02d" % room)


if __name__ == "__main__":
    main()
