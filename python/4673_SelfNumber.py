

def d(i: int, numList: list, count: int) -> int:
  if count <= i:
    return 0
  v: int = i

  while i:
    v += i % 10
    i //= 10

  if count <= v:
    return 0

  numList[v] = 1
  return d(v, numList, count)


def main():
  count: int = 10000
  numList: list = [0] * count
  for i in range(1, count):
    if numList[i] == 0:
      d(i, numList, count)
      print(i)


if __name__ == "__main__":
    main()
