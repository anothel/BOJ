from sys import stdin


def main():
  X_list = list()
  Y_list = list()

  pointX = 0
  pointY = 0

  for i in range(3):
    X, Y = map(int, stdin.readline().split())
    X_list.append(X)
    Y_list.append(Y)

  for j in range(3):
    countX = X_list.count(X_list[j])
    countY = Y_list.count(Y_list[j])
    if countX == 1:
      pointX = X_list[j]
    if countY == 1:
      pointY = Y_list[j]

  print(str(pointX), str(pointY))


if __name__ == "__main__":
    main()
