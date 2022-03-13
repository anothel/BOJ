from sys import stdin, stdout


def main():
  m, s, g = map(float, stdin.readline().rstrip().split())
  a, b = map(float, stdin.readline().rstrip().split())
  l, r = map(float, stdin.readline().rstrip().split())

  stdout.write(str("friskus" if m/g+l/a < m/s+r/b else "latmask"))


if __name__ == "__main__":
  main()
