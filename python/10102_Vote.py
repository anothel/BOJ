from sys import stdin


def main():
  A = 0
  B = 0

  V = int(stdin.readline().strip())
  votes = stdin.readline().strip()

  for i in range(V):
    if votes[i] == 'A':
      A += 1
    else:
      B += 1

  if A < B:
    print('B')
  elif B < A:
    print('A')
  else:
    print('Tie')


if __name__ == "__main__":
    main()
