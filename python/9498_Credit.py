import sys


def main():
  score = int(sys.stdin.readline())
  credit = "A"

  if 90 <= score and score <= 100:
    credit = "A"
  elif 80 <= score and score <= 89:
    credit = "B"
  elif 70 <= score and score <= 79:
    credit = "C"
  elif 60 <= score and score <= 69:
    credit = "D"
  else:
    credit = "F"

  print(credit)


if __name__ == "__main__":
    main()
