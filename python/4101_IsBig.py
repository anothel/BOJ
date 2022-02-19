from sys import stdin


def main():
  while 1:
    A, B = map(int, stdin.readline().split())
    if A == 0 and B == 0:
      break
    if B < A:
      print("Yes")
    else:
      print("No")


if __name__ == "__main__":
    main()
