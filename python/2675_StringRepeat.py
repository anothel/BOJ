import sys


def main():
  for i in range(int(sys.stdin.readline())):
    text = sys.stdin.readline().split()

    printText = ''
    for j in range(len(text[1])):
      for k in range(int(text[0])):
        printText += text[1][j]

    print(printText)


if __name__ == "__main__":
    main()
