from sys import stdin


def main():
  N = int(stdin.readline().rstrip())

  points: list = list(map(int, stdin.readline().split()))
  onePoint: list = sorted(list(set(points)))

  dic = {onePoint[i]: i for i in range(len(onePoint))}

  for i in points:
    print(dic[i], end=" ")


if __name__ == "__main__":
    main()
