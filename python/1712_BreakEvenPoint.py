from sys import stdin


def main():
  A, B, C = map(int, stdin.readline().strip().split())

  try:
    v = int(A / (C-B) + 1)
    if v < 0:
      print(-1)
    else:
      print(v)
  except:
    print(-1)


if __name__ == "__main__":
    main()
