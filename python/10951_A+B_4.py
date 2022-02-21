from sys import stdin


def main():
  while 1:
    try:
      A, B = map(int, stdin.readline().strip().split())
      if A <= 0 or 10 <= B:
        break
      print(str(A+B))
    except:
      break


if __name__ == "__main__":
    main()
