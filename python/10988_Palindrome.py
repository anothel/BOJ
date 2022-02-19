from sys import stdin


def main():
  word = stdin.readline().strip()
  result = 1
  l = len(word) - 1

  for i in range(l):
    if word[i] == word[l - i]:
      continue
    else:
      result = 0

  print(result)


if __name__ == "__main__":
    main()
