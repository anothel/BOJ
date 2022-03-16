from sys import stdin, stdout


def main():
  a, b, c, d = map(int, stdin.readline().strip().split())
  a1, b1, c1, d1 = map(int, stdin.readline().strip().split())

  if a1 + b1 + c1 + d1 < a+b+c+d:
    print(a+b+c+d)
  else:
    print(a1+b1+c1+d1)


if __name__ == "__main__":
    main()
