from sys import stdin


def main():
  for i in range(int(stdin.readline().strip())):
    A, B = map(int, stdin.readline().strip().split())
    print(A+B)


if __name__ == "__main__":
    main()
