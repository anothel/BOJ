from sys import stdin


def main():
  bodySpec: list = list()
  for _ in range(int(stdin.readline().strip())):
    bodySpec.append(list(map(int, stdin.readline().strip().split())))

  counts: list = list()
  for i in range(len(bodySpec)):
    count: int = 1
    for j in range(len(bodySpec)):
      if i == j:
        continue
      if bodySpec[i][0] < bodySpec[j][0] and bodySpec[i][1] < bodySpec[j][1]:
        count += 1

    counts.append(count)

  for count in counts:
    print(count, end=" ")


if __name__ == "__main__":
    main()
