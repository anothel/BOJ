from sys import stdin


def main():

  for i in range(int(stdin.readline())):
    r, e, c = map(int, stdin.readline().strip().split())

    if r < e-c:
      print("advertise")
    elif r == e-c:
      print("does not matter")
    else:
      print("do not advertise")


if __name__ == "__main__":
    main()
