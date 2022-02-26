from sys import stdin


def main():
  coords: list = list()
  for N in range(int(stdin.readline().rstrip())):
    tmp: list = list(map(int, stdin.readline().rstrip().split()))
    tmp.reverse()
    coords.append(tmp)

  coords.sort()
  for i in coords:
    print(str(i[1]) + " " + str(i[0]))


if __name__ == "__main__":
    main()
