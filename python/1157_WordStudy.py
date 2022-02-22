from sys import stdin


def main():
  wordList = list(stdin.readline().strip().upper())

  _newList = list()
  newList = list()
  for v in wordList:
    if v not in _newList:
      _newList.append(v)
      newList.append((v, wordList.count(v)))

  countList = list()
  for i in range(len(newList)):
    countList.append(newList[i][1])

  if 1 < countList.count(max(countList)):
    print('?')
  else:
    for i in range(len(newList)):
      if newList[i][1] == max(countList):
        print(_newList[i])
        break


if __name__ == "__main__":
    main()
