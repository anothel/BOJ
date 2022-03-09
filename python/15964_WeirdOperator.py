from sys import stdin, stdout


def main():
  A, B = map(int, stdin.readline().strip().split())
  stdout.write(str((A+B)*(A-B)))


if __name__ == "__main__":
    main()
