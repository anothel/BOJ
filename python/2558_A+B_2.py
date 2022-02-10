import sys


def main():
  data = [sys.stdin.readline().strip() for i in range(2)]
  print(int(data[0]) + int(data[1]))


if __name__ == "__main__":
    main()
