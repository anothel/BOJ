from sys import stdin


def main():

  for i in range(int(stdin.readline().strip())):
    total = 0
    score = 0
    text = stdin.readline().strip()
    for j in range(len(text)):
      if text[j] == 'O':
        total += (score + 1)
        score += 1
      else:
        score = 0

    print(total)


if __name__ == "__main__":
    main()
