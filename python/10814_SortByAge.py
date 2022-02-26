from operator import itemgetter
from sys import stdin


def main():
  members: list = list()
  for N in range(int(stdin.readline().strip())):
    # member.append(str(N))
    members.append(list(stdin.readline().strip().split()))

  for member in sorted(members, key=lambda x: int(x[0])):
    print(member[0] + " " + member[1])


if __name__ == "__main__":
    main()
