from sys import stdin, stdout


def main():
  nYear: int = int(stdin.readline().strip())
  stdout.write(str(nYear - 1946))


if __name__ == "__main__":
    main()
