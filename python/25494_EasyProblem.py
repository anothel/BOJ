from sys import stdin, stdout


def solution():
    for _ in range(int(stdin.readline().rstrip())):
        answer: int = 0
        a, b, c = map(int, stdin.readline().rstrip().split())
        for i in range(1, a + 1):
            for j in range(1, b + 1):
                for k in range(1, c + 1):
                    if i % j == j % k == k % i:
                        answer += 1
        stdout.write("%d\n" % answer)

if __name__ == "__main__":
    solution()
