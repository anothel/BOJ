from sys import stdin


def main():
  K, N, M = map(int, stdin.readline().split())
  print(K * N - M)


if __name__ == "__main__":
    main()
