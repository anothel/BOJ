from sys import stdin


def main():
  S = int(stdin.readline())

  N = 0
  i = 1

  while 1:
    S -= i
    i += 1
    N += 1
    if S < i:
      break
  print(N)


if __name__ == "__main__":
    main()
