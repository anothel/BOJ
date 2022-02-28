from sys import stdin, stdout


def main():
  n, m = map(int, stdin.readline().strip().split())
  stdout.write(str(n // m) + "\n")
  stdout.write(str(n % m) + "\n")
  # print(n // m)
  # print(n % m)


if __name__ == "__main__":
    main()
