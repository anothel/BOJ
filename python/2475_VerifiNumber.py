from sys import stdin


def main():
  inputList = list(map(int, stdin.readline().strip().split()))
  sum = 0
  for i in inputList:
    sum += (i * i)
  print(sum % 10)


if __name__ == "__main__":
    main()
