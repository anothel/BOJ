from sys import stdin


def prime_list(n: int) -> list:
  primeList: list = [True] * n

  for i in range(2, n):
    if primeList[i] == True:
      for j in range(i + i, n, i):
        primeList[j] = False

  return [i for i in range(2, n) if primeList[i] == True]


def main():
  M = int(stdin.readline().strip())
  N = int(stdin.readline().strip())

  primeList: list = prime_list(N + 1)

  sum: int = 0
  min: int = 0
  isMin: bool = True

  for i in primeList:
    if M <= i and i <= N:
      if isMin == True:
        min = i
        isMin = False
      sum += i

  if sum == 0:
    print(-1)
  else:
    print(sum)
    print(min)


if __name__ == "__main__":
    main()
