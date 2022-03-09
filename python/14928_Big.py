from sys import stdin, stdout


def main():
  n = int(stdin.readline().strip())

  stdout.write(str(n % 20000303))


if __name__ == "__main__":
    main()
