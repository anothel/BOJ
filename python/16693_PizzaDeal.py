from sys import stdin, stdout


def main():
  pi: float = 3.14159265359
  a1, p1 = map(int, stdin.readline().strip().split())
  r1, p2 = map(int, stdin.readline().strip().split())

  x = a1 * p2 / (pi * (r1 ** 2))

  stdout.write(str("Whole pizza" if p1 > x else "Slice of pizza"))


if __name__ == "__main__":
    main()
