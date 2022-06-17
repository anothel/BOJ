from sys import stdin, stdout


def solution():
  vk, jk = map(int, stdin.readline().rstrip().split())
  vl, jl = map(int, stdin.readline().rstrip().split())
  vh, dh, jh = map(int, stdin.readline().rstrip().split())

  stdout.write("%d" % ((vk * jk + vl * jl) * vh * dh * jh))


if __name__ == "__main__":
  solution()
