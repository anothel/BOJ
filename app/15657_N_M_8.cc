#include <algorithm>
#include <iostream>
#include <vector>

enum : int { MAX_NUM = 8 };

static int N(0), M(0), Input(0);
static std::vector<int> vAnswer;
static std::vector<int> vInput;
static bool bVisited[MAX_NUM];

void dfs(const int& count, const int& num) {
  if (M == count) {
    for (int i = 0; i < M; i++) std::cout << vAnswer[i] << " ";
    std::cout << "\n";

    return;
  }

  for (int i = num; i < N; i++) {
    vAnswer.push_back(vInput.at(i));
    dfs(count + 1, i);
    vAnswer.pop_back();
  }

  return;
}

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);
  std::cin >> N >> M;

  for (int i = 0; i < N; i++) {
    std::cin >> Input;
    vInput.push_back(Input);
  }
  sort(vInput.begin(), vInput.end());

  dfs(0, 0);

  return 0;
}