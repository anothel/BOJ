from sys import stdin


def main():
  A, B = map(int, stdin.readline().strip().split())

  if A < B:
    print('<')
  elif B < A:
    print('>')
  else:
    print('==')


if __name__ == "__main__":
    main()
