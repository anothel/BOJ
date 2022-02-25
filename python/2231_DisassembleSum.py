from sys import stdin


def findSum(n: int) -> int:
  nReturnValue: int = n

  for i in range(len(str(n))):
    nReturnValue += n % 10
    n //= 10

  return nReturnValue


def main():
  N = int(stdin.readline().strip())
  i: int = 1
  bPass = False
  while i < N:
    if findSum(i) == N:
      bPass = True
      break
    i += 1
  if bPass == True:
    print(i)
  else:
    print(0)


if __name__ == "__main__":
    main()
