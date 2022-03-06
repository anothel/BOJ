from sys import stdin, stdout


def main():
  A = int(stdin.readline().strip())
  B = int(stdin.readline().strip())

  stdout.write(str(A+B) + "\n")
  stdout.write(str(A-B) + "\n")
  stdout.write(str(A*B) + "\n")


if __name__ == "__main__":
    main()
