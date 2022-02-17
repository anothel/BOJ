import sys


def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False


def main():
  for i in range(int(sys.stdin.readline())):
    text = sys.stdin.readline().split()

    number = 0
    op = ''

    for j in range(len(text)):
      currnetText = text[j]

      if isNumber(currnetText):
        number = float(currnetText)
      else:
        op = currnetText
        if op == '@':
          number *= 3
        elif op == '%':
          number += 5
        elif op == '#':
          number -= 7
        else:
          print(op)

    print("{:.2f}".format(number))


if __name__ == "__main__":
    main()
