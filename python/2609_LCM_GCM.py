from sys import stdin, stdout


def gcd(a: int, b: int) -> int:
  if b == 0:
    return a
  else:
    return gcd(b, a % b)


def lcm(a: int, b: int) -> int:
  return (a * b) // gcd(a, b)


def main():
  a, b = map(int, stdin.readline().strip().split())
  stdout.write(str(gcd(a, b)) + "\n")
  stdout.write(str(lcm(a, b)) + "\n")


if __name__ == "__main__":
    main()
