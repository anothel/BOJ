from sys import stdin


def prime_list(n: int) -> list:
  primeList: list = [True] * n

  for i in range(2, n):
    if primeList[i] == True:
      for j in range(i + i, n, i):
        primeList[j] = False

  return [i for i in range(2, n) if primeList[i] == True]


def bertran(n: int, l: list) -> int:
  count: int = 0
  for i in l:
    if n < i and i <= 2 * n:
      count += 1
  return count


def main():
  primeList: list = prime_list(123456 * 2 + 1)
  
  while True:
    n = int(stdin.readline().strip())
    if n == 0:
      break

    print(bertran(n, primeList))


if __name__ == "__main__":
    main()
