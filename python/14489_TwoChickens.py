from sys import stdin, stdout


def main():
  moneys: list = list(map(int, stdin.readline().rstrip().split()))
  chicken: int = int(stdin.readline().rstrip())

  allMoney: int = sum(moneys)
  chicken *= 2
  if allMoney >= chicken:
    stdout.write(str(allMoney - chicken))
  else:
    stdout.write(str(allMoney))


if __name__ == "__main__":
    main()
