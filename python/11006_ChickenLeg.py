from sys import stdin, stdout


def main():
  for _ in range(int(stdin.readline().rstrip())):
    n, m = map(int, stdin.readline().rstrip().split())
    stdout.write(str(2*m-n) + " " + str(m-(2*m-n)) + "\n")


if __name__ == "__main__":
    main()
