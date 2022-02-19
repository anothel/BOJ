from sys import stdin


def main():
  total = 0
  for i in range(5):
    score = int(stdin.readline())
    if score < 40:
      score = 40
    total += score
  print(total // 5)


if __name__ == "__main__":
    main()
