from sys import stdin, stdout


def main():
  countList: list = list()
  for T in range(int(stdin.readline().strip())):
    countList.append(int(stdin.readline().strip()))

  for i in countList:
    if i % 10 == 0:
      stdout.write(str(1) + "\n")
    else:
      stdout.write(str(0) + "\n")


if __name__ == "__main__":
  main()
