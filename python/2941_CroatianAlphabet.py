from sys import stdin


def main():
  sum: int = 0
  wordList = stdin.readline().strip()

  sum += wordList.count('c=')
  wordList = wordList.replace('c=', " ")
  
  sum += wordList.count('c-')
  wordList = wordList.replace('c-', " ")
  
  sum += wordList.count('dz=')
  wordList = wordList.replace('dz=', " ")
  
  sum += wordList.count('d-')
  wordList = wordList.replace('d-', " ")
  
  sum += wordList.count('lj')
  wordList = wordList.replace('lj', " ")
  
  sum += wordList.count('nj')
  wordList = wordList.replace('nj', " ")
  
  sum += wordList.count('s=')
  wordList = wordList.replace('s=', " ")
  
  sum += wordList.count('z=')
  wordList = wordList.replace('z=', " ")

  wordList = wordList.replace(' ', "")

  print(sum + len(wordList))


if __name__ == "__main__":
    main()
