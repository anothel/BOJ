from sys import stdin


def main():
  score_A = 100
  score_B = 100
  for n in range(int(stdin.readline())):
    A, B = map(int, stdin.readline().split())
    if A < B:
      score_A -= B
    elif B < A:
      score_B -= A

  print(score_A)
  print(score_B)


if __name__ == "__main__":
    main()
