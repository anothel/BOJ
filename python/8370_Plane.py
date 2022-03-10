from sys import stdin, stdout


def main():
  n1, k1, n2, k2 = map(int, stdin.readline().strip().split())

  stdout.write(str((n1 * k1) + (n2 * k2)))


if __name__ == "__main__":
    main()
