from sys import stdin


def findStars(n: int, stars: list) -> list:
  lStars: list = list()
  if n == 3:
    return stars
  else:
    for i in stars:
      lStars.append(i*3)
    for i in stars:
      lStars.append(i + " " * len(stars) + i)
    for i in stars:
      lStars.append(i*3)
  return findStars(n//3, lStars)


def main():
  for stars in findStars(int(stdin.readline().strip()), ['***', '* *', '***']):
    print(stars)


if __name__ == "__main__":
    main()
