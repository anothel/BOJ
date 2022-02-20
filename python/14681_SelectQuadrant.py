from sys import stdin


def main():
  data = [stdin.readline().strip() for i in range(2)]
  
  X = int(data[0])
  Y = int(data[1])
  
  if 0 < X and 0 < Y:
    print(1)
  elif X < 0 and 0 < Y:
    print(2)
  elif X < 0 and Y < 0:
    print(3)
  elif 0 < X and Y < 0:
    print(4)


if __name__ == "__main__":
    main()
