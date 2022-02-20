from sys import stdin


def check(qList):
  for n in range(int(stdin.readline().strip())):
    X, Y = map(int, stdin.readline().strip().split())

    if 0 < X and 0 < Y:
      qList[0] += 1
    elif X < 0 and 0 < Y:
      qList[1] += 1
    elif X < 0 and Y < 0:
      qList[2] += 1
    elif 0 < X and Y < 0:
      qList[3] += 1
    else:
      qList[4] += 1


def main():
  qList = [0, 0, 0, 0, 0]

  check(qList)

  print("Q1: " + str(qList[0]))
  print("Q2: " + str(qList[1]))
  print("Q3: " + str(qList[2]))
  print("Q4: " + str(qList[3]))
  print("AXIS: " + str(qList[4]))


if __name__ == "__main__":
    main()
