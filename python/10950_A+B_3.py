from sys import stdin


def main():
  for T in range(int(stdin.readline().strip())):
    A, B = map(int, stdin.readline().strip().split())
    print(str(A+B))


if __name__ == "__main__":
    main()
