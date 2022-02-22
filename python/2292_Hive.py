from sys import stdin


def main():
  N = int(stdin.readline().strip())

  i = 0
  v = 1
  while 1:
    v += 6 * i
    if N <= v:
      print(i + 1)
      break
    i += 1


if __name__ == "__main__":
    main()
