from sys import stdin, stdout


def main():
  stdout.write(str(sum(list(map(int, stdin.readline().rstrip().split())))))


if __name__ == "__main__":
    main()
