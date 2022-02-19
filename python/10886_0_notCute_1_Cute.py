from sys import stdin


def main():
  c = 0
  nc = 0
  for i in range(int(stdin.readline())):
    v = int(stdin.readline())
    if v == 1:
      c += 1
    elif v == 0:
      nc += 1
  if nc < c:
    print("Junhee is cute!")
  else:
    print("Junhee is not cute!")


if __name__ == "__main__":
    main()
