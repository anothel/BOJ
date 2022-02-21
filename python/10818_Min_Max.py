from sys import stdin


def main():
  N = int(stdin.readline().strip())
  nList = list(map(int, stdin.readline().strip().split()))
  print(str(min(nList)) + " " + str(max(nList)))


if __name__ == "__main__":
    main()
