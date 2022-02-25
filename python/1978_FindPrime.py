from sys import stdin


def prime_list(n: int) -> list:
  primeList: list = [True] * n
  
  for i in range(2, n):
    if primeList[i] == True:
      for j in range(i + i, n, i):
        primeList[j] = False
  
  return [i for i in range(2, n) if primeList[i] == True]


def main():
  int(stdin.readline().strip())
  primeList: list = prime_list(1001)
  count: int = 0
  for i in list(map(int, stdin.readline().strip().split())):
    if primeList.count(i) == 1:
      count += 1
  print(count)


if __name__ == "__main__":
    main()
