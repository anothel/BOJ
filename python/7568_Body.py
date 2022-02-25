from sys import stdin


def getCountList(bodies: list) -> list:
  lReturnValue: list = list()

  for i in range(len(bodies)):
    count: int = 1
    for j in range(len(bodies)):
      if i == j:
        continue
      if bodies[i][0] < bodies[j][0] and bodies[i][1] < bodies[j][1]:
        count += 1
    lReturnValue.append(count)

  return lReturnValue


def main():
  bodies: list = list()
  for _ in range(int(stdin.readline().strip())):
    bodies.append(list(map(int, stdin.readline().strip().split())))

  for count in getCountList(bodies):
    print(count, end=" ")


if __name__ == "__main__":
    main()
