from sys import stdin, stdout


def main():
  n: int = int(stdin.readline().rstrip())
  students: list = list(map(int, stdin.readline().rstrip().split()))

  count: int = 0
  for i in range(n):
    if students[i] != i+1:
      count += 1

  stdout.write(str(count))


if __name__ == "__main__":
    main()
