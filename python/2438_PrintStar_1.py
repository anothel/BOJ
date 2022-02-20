from sys import stdin


def main():
  star = list()
  for i in range(int(stdin.readline())):
    s = ''
    star.append('*')
    print(s.join(star))


if __name__ == "__main__":
    main()
