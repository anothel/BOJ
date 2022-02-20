from sys import stdin


def main():
  N = int(stdin.readline())

  for i in range(9):
    print(str(N) + " * " + str(i + 1) + " = " + str(N * (i + 1)))


if __name__ == "__main__":
    main()
