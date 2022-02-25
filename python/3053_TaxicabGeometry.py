from sys import stdin


def main():
  pi: float = 3.14159265359
  R = int(stdin.readline().strip())

  print("%.06f" % float(R*R*pi))
  print("%.06f" % float(R*R*2))


if __name__ == "__main__":
    main()
