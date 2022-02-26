from sys import stdin
from sys import stdout


def main():

  maxNum: int = 10000
  count: list = [0] * (maxNum + 1)

  for _ in range(int(stdin.readline().rstrip())):
    count[int(stdin.readline().rstrip())] += 1

  for i in range(1, maxNum + 1):
    for _ in range(count[i]):
      stdout.write(str(i) + "\n")


if __name__ == "__main__":
    main()
