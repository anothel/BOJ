from sys import stdin


def getMin(x: int, w: int) -> int:
  min: int = 0

  if x <= w // 2:
    min = x
  else:
    min = w - x


  return min


def main():
  x, y, w, h = map(int, stdin.readline().strip().split())

  minX: int = getMin(x, w)
  min: int = minX

  minY: int = getMin(y, h)

  if minY < min:
    min = minY

  print(min)


if __name__ == "__main__":
    main()
