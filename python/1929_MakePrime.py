from sys import stdin


def prime_list(n: int) -> list:
  primeList: list = [True] * n

  for i in range(2, n):
    if primeList[i] == True:
      for j in range(i + i, n, i):
        primeList[j] = False

  return [i for i in range(2, n) if primeList[i] == True]


def main():
  M, N = map(int, stdin.readline().strip().split())

  primeList: list = prime_list(N + 1)

  for i in primeList:
    if M <= i and i <= N:
      print(i)


if __name__ == "__main__":
    main()
