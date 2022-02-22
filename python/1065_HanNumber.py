from sys import stdin


def isHan(n):
  bHan = False
  numList = list()

  while n:
    numList.insert(0, n % 10)
    n //= 10

  if len(numList) == 1 or len(numList) == 2:
    bHan = True
  elif len(numList) == 3 and numList[2] - numList[1] == numList[1] - numList[0]:
    bHan = True

  return bHan


def main():
  count = 0

  for i in range(1, int(stdin.readline().strip()) + 1):
    if isHan(i) == True:
      count += 1

  print(count)


if __name__ == "__main__":
    main()
