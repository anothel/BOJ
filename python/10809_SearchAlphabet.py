from sys import stdin


def main():
  input = list(stdin.readline().strip())

  alphabet = list()
  for i in range(ord('a'), ord('z') + 1):
    insert = -1
    for j in range(len(input)):
      if input[j] == chr(i):
        insert = j
        break
    alphabet.append((chr(i), insert))

  for i in range(len(alphabet)):
    print(alphabet[i][1], end=' ')


if __name__ == "__main__":
    main()
