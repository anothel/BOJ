#include <cstdlib>
#include <iostream>
#include <vector>

void check(std::vector<int> vPieces, const std::vector<int>& vCounts) {
  // for (auto iter = std::begin(vPieces); iter != std::end(vPieces); iter++) {
  //   std::cout << *iter << std::endl;
  // }
  for (auto i = 0; i < vPieces.size(); i++) {
    std::cout << vCounts[i] - vPieces[i] << " ";
  }

  return;
}

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  std::vector<int> vPieces, vCounts = {1, 1, 2, 2, 2, 8};
  for (int i = 0; i < 6; i++) {
    int nPiece = 0;
    std::cin >> nPiece;
    vPieces.push_back(nPiece);
  }

  check(vPieces, vCounts);

  return 0;
}
