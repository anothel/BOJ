from sys import stdin


def main():
  for T in range(int(stdin.readline())):
    alcohol_list = list()
    for N in range(int(stdin.readline())):
      text = stdin.readline().split()
      alcohol_list.insert(0, (int(text[1]), text[0]))
    alcohol_list = sorted(alcohol_list)

    print(alcohol_list[len(alcohol_list)-1][1])


if __name__ == "__main__":
    main()
