from sys import stdin


def prime_list(n: int) -> list:
  primeList: list = [True] * n

  for i in range(2, n):
    if primeList[i] == True:
      for j in range(i + i, n, i):
        primeList[j] = False

  return [i for i in range(2, n) if primeList[i] == True]


def printPartition(n: int, primeList: list):
  half: int = n // 2

  if primeList.count(half) == 1:
    print(str(half) + " " + str(half))
    return

  startIndex: int = 0
  for i in range(0, len(primeList)):
    if primeList[i] <= half and half <= primeList[i+1]:
      startIndex = i
      break

  for i in range(startIndex + 1, len(primeList)):
    for j in range(startIndex, 0, -1):
      if primeList[i] + primeList[j] == n:
        print(str(primeList[j]) + " " + str(primeList[i]))
        return

  return


def main():
  nums: list = list()
  for T in range(int(stdin.readline().strip())):
    nums.append(int(stdin.readline().strip()))

  printList: list = prime_list(max(nums))
  for i in nums:
    printPartition(i, printList)


if __name__ == "__main__":
    main()
