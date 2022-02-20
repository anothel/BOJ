from sys import stdin


def main():
  N = int(stdin.readline())

  star = list()
  for i in range(N):
    star.append(' ')

  for i in range(N):
    s = ''
    star[N - 1 - i] = '*'
    print(s.join(star))


if __name__ == "__main__":
    main()
