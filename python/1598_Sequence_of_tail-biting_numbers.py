from sys import stdin, stdout


def main():
  a, b = map(int, stdin.readline().rstrip().split())
  a_ = (a % 4) if (a % 4) != 0 else 4
  b_ = (b % 4) if (b % 4) != 0 else 4

  if a % 4 == 0:
    a = a // 4 - 1
  else:
    a = a // 4
  if b % 4 == 0:
    b = b // 4 - 1
  else:
    b = b // 4

  stdout.write(str(abs(a - b) + abs((a_) - (b_))))


if __name__ == "__main__":
  main()
