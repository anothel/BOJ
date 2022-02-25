from sys import stdin


def getPalPal(m: int, n: int, input: list) -> list:
  lReturnValue: list = list()

  for i in range(m, m + 8):
    lN: list = list()
    for j in range(n, n + 8):
      lN.append(input[i][j])
    lReturnValue.append(lN)

  return lReturnValue


def getCountPaint(input: list) -> int:
  nReturnValue: int = 0

  tmp: list = list()
  # tmp:list = list(input)
  for i in input:
    tmp.append(i.copy())
    # tmp.append(i[:])

  for i in range(8):
    if i < 7 and not(tmp[i+1][0] ^ tmp[i][0]):
      tmp[i + 1][0] = not tmp[i][0]
      nReturnValue += 1
    for j in range(7):
      if not(tmp[i][j+1] ^ tmp[i][j]):
        tmp[i][j+1] = not tmp[i][j]
        nReturnValue += 1

  # print(input)

  return nReturnValue


def main():
  chessBoard: list = list()

  M, N = map(int, stdin.readline().strip().split())

  for _ in range(M):
    # inputList: list = list()
    # for i in list(stdin.readline().strip()):
    #     inputList.append(i != "W")
    # chessBoard.append(inputList)
    chessBoard.append(
        list(map(lambda x: False if x == 'W' else True, list(stdin.readline().strip()))))
  # print(chessBoard)

  min: int = -1

  m: int = 0
  while m + 7 < M:
    n: int = 0
    while n + 7 < N:
      lPalPal: list = list(getPalPal(m, n, chessBoard))
      count: int = getCountPaint(lPalPal)
      lPalPal[0][0] = not lPalPal[0][0]
      if getCountPaint(lPalPal) + 1 < count:
        count = getCountPaint(lPalPal) + 1
      if min == -1 or count < min:
        min = count
      if min == 0:
        print(0)
        return
      n += 1
    m += 1

  print(min)


if __name__ == "__main__":
    main()
