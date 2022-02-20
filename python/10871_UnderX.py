from sys import stdin


def main():
  N, X = map(int, stdin.readline().strip().split())
  n_list = list(map(int, stdin.readline().strip().split()))

  for i in n_list:
    if i < X:
      print(i, end=' ')


if __name__ == "__main__":
    main()
