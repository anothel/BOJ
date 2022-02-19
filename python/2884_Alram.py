from sys import stdin


def main():
  h, m = map(int, stdin.readline().strip().split())

  m -= 45
  if m < 0:
    m += 60
    h -= 1

  if h < 0:
    h += 24

  print(str(h) + " " + str(m))


if __name__ == "__main__":
    main()
