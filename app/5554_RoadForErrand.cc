#include <iostream>

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  int nTotal = 0;
  for (int i = 0; i < 4; i++) {
    int nScore = 0;
    std::cin >> nScore;
    nTotal += nScore;
  }

  std::cout << nTotal / 60 << "\n";
  std::cout << nTotal % 60 << "\n";

  return 0;
}
