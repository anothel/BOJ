from sys import stdin


def main():
  price = 0
  maxPrice = 0
  for i in range(int(stdin.readline())):
    A, B, C = map(int, stdin.readline().split())
    if A == B == C:
      price = 10000 + A * 1000
    elif A == B or A == C:
      price = 1000 + A * 100
    elif B == C:
      price = 1000 + B * 100
    else:
      dice_list = list()
      dice_list.insert(0, A)
      dice_list.insert(0, B)
      dice_list.insert(0, C)
      dice_list.sort()
      price = dice_list[2] * 100

    if maxPrice < price:
      maxPrice = price

  print(maxPrice)


if __name__ == "__main__":
    main()
