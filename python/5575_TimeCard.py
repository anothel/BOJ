from sys import stdin, stdout
import datetime


def main():
  for _ in range(3):
    h, m, s, h1, m1, s1 = map(int, stdin.readline().strip().split())
    dt = datetime.datetime(2022, 3, 16, h1, m1, s1) - \
        datetime.datetime(2022, 3, 16, h, m, s)
    stdout.write(str(dt.seconds // 3600) + " " +
                 str((dt.seconds % 3600) // 60) + " " + str(dt.seconds % 60) + "\n")


if __name__ == "__main__":
    main()
