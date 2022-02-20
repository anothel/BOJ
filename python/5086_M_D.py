from sys import stdin


def main():
  while 1:
    A, B = map(int, stdin.readline().split())
    if A == 0 and B == 0:
      break

    if B % A == 0:
      print("factor")
    elif A % B == 0:
      print("multiple")
    else:
      print("neither")


if __name__ == "__main__":
    main()
