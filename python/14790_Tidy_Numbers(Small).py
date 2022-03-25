from sys import stdin, stdout


def isClean(number: int) -> bool:
  before: int = number % 10
  number //= 10
  while number > 0:
    if before >= number % 10:
      before = number % 10
      number //= 10
      continue
    else:
      return False
  return True


def main():
  for i in range(int(stdin.readline().strip())):
    a = int(stdin.readline().strip())

    for j in range(a, 0, -1):
      if isClean(j) == True:
        stdout.write(str("Case #%d: " % (i+1) + str(j) + "\n"))
        break


if __name__ == "__main__":
    main()
