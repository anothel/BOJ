from sys import stdin


def getAverage(scores):
  sum = 0
  for j in range(1, len(scores)):
    sum += scores[j]
  return sum / scores[0]


def main():
  for i in range(int(stdin.readline().strip())):
    scores = list(map(int, stdin.readline().strip().split()))

    average = getAverage(scores)

    count = 0
    for j in range(1, len(scores)):
      if average < scores[j]:
        count += 1

    print('%.3f' % (count / scores[0] * 100) + '%')


if __name__ == "__main__":
    main()
