from sys import stdin


def prime_list(n: int) -> list:
  primeList: list = [True] * n

  for i in range(2, n):
    if primeList[i] == True:
      for j in range(i + i, n, i):
        primeList[j] = False

  return [i for i in range(2, n) if primeList[i] == True]


def printPartition(n: int, primeList: list):
  s: int = 0
  b: int = 0
  diff: int = -1

  half: int = n // 2

  if primeList.count(half) == 1:
    print(str(half) + " " + str(half))
    return

  startIndex: int = 0
  # print("half: " + str(half))
  for i in range(0, len(primeList)):    
    if primeList[i] <= half and half <= primeList[i+1]:
      startIndex = i
      break

  for i in range(startIndex + 1, len(primeList)):
    for j in range(startIndex, 0, -1):
      # print("i: " + str(i) + ", j: " + str(j))
      if primeList[i] + primeList[j] == n:
        print(str(primeList[j]) + " " + str(primeList[i]))
        return

  # for i in range(len(primeList)):
  #   if n <= primeList[i] or diff == 0:
  #     break
  #   for j in range(i, len(primeList)):
  #     sum = primeList[i] + primeList[j]
  #     if sum == n:
  #       if diff == -1 or primeList[j] - primeList[i] < diff:
  #         diff = primeList[j] - primeList[i]
  #         s = primeList[i]
  #         b = primeList[j]
  #       elif diff == 0:
  #         break
  #     elif n < sum:
  #       break

  # print(str(s) + " " + str(b))
  return


def main():
  nums = list()
  for T in range(int(stdin.readline().strip())):
    nums.append(int(stdin.readline().strip()))

  printList: list = prime_list(max(nums))
  # print(printList)
  for i in nums:
    printPartition(i, printList)

  # for T in range(int(stdin.readline().strip())):
  #   printPartition(int(stdin.readline().strip()), primeList)


if __name__ == "__main__":
    main()
