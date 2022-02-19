from sys import stdin


def main():
  T = int(stdin.readline())

  countA = 0
  countB = 0
  countC = 0

  while T:
    if 300 <= T:
      T -= 300
      countA += 1
    else:
      break

  while T:
    if 60 <= T:
      T -= 60
      countB += 1
    else:
      break

  while T:
    if 10 <= T:
      T -= 10
      countC += 1
    else:
      break
  if T == 0:
    print('%d %d %d' % (countA, countB, countC))
  else:
    print(-1)


if __name__ == "__main__":
    main()
