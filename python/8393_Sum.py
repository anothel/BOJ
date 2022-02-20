from sys import stdin


def main():
  sum = 0
  for i in range(int(stdin.readline())):
    sum += (i+1)

  print(sum)


if __name__ == "__main__":
    main()
