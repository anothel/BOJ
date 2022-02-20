from sys import stdin


def main():
  for i in range(int(stdin.readline().strip())):
    scores = list(map(int, stdin.readline().strip().split()))

    sum = 0
    for j in range(1, len(scores)):
      sum += scores[j]
    average = sum / scores[0]

    count = 0
    for j in range(1, len(scores)):
      if average < scores[j]:
        count += 1

    print('%.3f' % (count / scores[0] * 100) + '%')


if __name__ == "__main__":
    main()
