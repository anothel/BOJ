#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  std::vector<int> vTriangle;
  int nTotal = 0;
  for (int i = 0; i < 3; i++) {
    int nCorner = 0;
    std::cin >> nCorner;
    vTriangle.push_back(nCorner);
    nTotal += nCorner;
  }

  if (nTotal == 180) {
    if (vTriangle[0] == 60 && vTriangle[1] == 60 && vTriangle[2] == 60) {
      std::cout << "Equilateral \n";
    } else if (vTriangle[0] == vTriangle[1] || vTriangle[1] == vTriangle[2] ||
               vTriangle[0] == vTriangle[2]) {
      std::cout << "Isosceles \n";
    } else {
      std::cout << "Scalene \n";
    }
  } else {
    std::cout << "Error \n";
  }

  return 0;
}
