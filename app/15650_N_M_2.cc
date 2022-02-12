#include <iostream>
#include <vector>

enum : int { MAX_NUM = 8 };

static int N(0), M(0);
static std::vector<int> vAnswer;
static bool bVisited[MAX_NUM] = {0};;

void dfs(const int& count, const int& num) {
  if (count == M) {
    for (int i = 0; i < M; i++) std::cout << vAnswer[i] << " ";
    std::cout << "\n";

    return;
  }

  for (int i = num; i < N; i++) {
    if (bVisited[i] == false) {
      bVisited[i] = true;
      vAnswer.push_back(i + 1);
      dfs(count + 1, i);
      vAnswer.pop_back();
      bVisited[i] = false;
    }
  }

  return;
}

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  std::cin >> N >> M;

  dfs(0, 0);

  return 0;
}
