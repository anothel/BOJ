from sys import stdin


def main():
  r = 1
  numList = [0] * 10
  # numList = [0 for _ in range(10)]

  for _ in range(3):
    r *= int(stdin.readline().strip())

  while 0 < r:
    numList[r % 10] += 1
    r //= 10

  for i in range(10):
    print(numList[i])


if __name__ == "__main__":
    main()
