from sys import stdin


def main():
  while 1:
    M, F = map(int, stdin.readline().split())
    if M == 0 and F == 0:
      break
    print(M + F)


if __name__ == "__main__":
    main()
