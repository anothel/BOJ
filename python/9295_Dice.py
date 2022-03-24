from sys import stdin, stdout


def main():
  for i in range(int(stdin.readline().rstrip())):
    a, b = map(int, stdin.readline().rstrip().split())
    stdout.write("Case %d: " % (i + 1) + str(a + b) + "\n")


if __name__ == "__main__":
    main()
