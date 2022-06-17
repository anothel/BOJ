from sys import stdin, stdout


def prime_list(n: int) -> list:
  primeList: list = [True] * n

  for i in range(2, n):
    if primeList[i] == True:
      for j in range(i + i, n, i):
        primeList[j] = False

  return [i for i in range(2, n) if primeList[i] == True]


def main():
  P, k = map(int, stdin.readline().strip().split())

  primeList: list = prime_list(k)

  result: str = "GOOD"
  for i in primeList:
    if P % i == 0:
      result = "BAD %d" % i
      break

  stdout.write(str(result))


if __name__ == "__main__":
    main()
