from email.base64mime import header_length
from sys import stdin


def main():
  text = stdin.readline().strip()

  height = 0
  plate = ' '

  for i in range(len(text)):
    if i == 0:
      height = 10
      plate = text[0]
      continue

    if plate == text[i]:
      height += 5
    else:
      height += 10

    plate = text[i]

  print(height)


if __name__ == "__main__":
    main()
