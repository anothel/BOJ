from sys import stdin


def main():
  credit = stdin.readline()
  myScore = 0
  frontScore = [('A', 4), ('B', 3), ('C', 2), ('D', 1), ('F', 0)]
  rearScore = [('+', 0.3), ('0', 0), ('-', -0.3)]

  for i in range(len(frontScore)):
    if credit[0] == frontScore[i][0]:
      myScore += frontScore[i][1]

  for i in range(len(rearScore)):
    if credit[1] == rearScore[i][0]:
      myScore += rearScore[i][1]

  print('%.1f' % (myScore))


if __name__ == "__main__":
    main()
