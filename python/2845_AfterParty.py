from sys import stdin, stdout


def main():
  S, P = map(int, stdin.readline().strip().split())
  Counts: list = list(map(int, stdin.readline().strip().split()))

  for i in Counts:
    stdout.write(str(i - (S*P)) + " ")


if __name__ == "__main__":
    main()
