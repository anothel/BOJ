from sys import stdin


def main():
  nList = list()
  for _ in range(9):
    nList.append(int(stdin.readline().strip()))

  print(max(nList))
  print(nList.index(max(nList)) + 1)


if __name__ == "__main__":
    main()
