from sys import stdin


def hanoi(number_of_disks_to_move, from_, to_, via_, l: list):
    if number_of_disks_to_move == 1:
      l.append(str(from_) + " " + str(to_))
    else:
      hanoi(number_of_disks_to_move-1, from_, via_, to_, l)
      l.append(str(from_) + " " + str(to_))
      hanoi(number_of_disks_to_move-1, via_, to_, from_, l)


def main():
  printList: list = list()
  hanoi(int(stdin.readline().strip()), 1, 3, 2, printList)
  print(len(printList))
  for s in printList:
    print(s)


if __name__ == "__main__":
    main()
