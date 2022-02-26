from sys import stdin


def main():
  coords: list = list()
  for N in range(int(stdin.readline().rstrip())):
    coords.append(list(map(int, stdin.readline().rstrip().split())))

  coords.sort()
  for i in coords:
    print(str(i[0]) + " " + str(i[1]))


if __name__ == "__main__":
    main()
