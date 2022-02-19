from sys import stdin


def main():
  K, N, M = map(int, stdin.readline().split())
  needMoney = K * N - M
  if needMoney < 0:
    needMoney = 0

  print(needMoney)


if __name__ == "__main__":
    main()
