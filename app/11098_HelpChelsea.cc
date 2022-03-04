#include <iostream>
#include <string>
#include <utility>
#include <vector>

void printMostExpensive() {
  int p = 0;
  std::cin >> p;

  std::vector<std::pair<int, std::string>> vBucket;
  int nMax = 0;

  for (int i = 0; i < p; i++) {
    int C;
    std::string sName;
    std::cin >> C >> sName;
    if (nMax < C) {
      nMax = C;
    }
    vBucket.push_back(std::pair(C, sName));
  }

  std::vector<std::pair<int, std::string>>::iterator iter;
  for (iter = vBucket.begin(); iter != vBucket.end(); iter++) {
    if ((*iter).first == nMax) {
      std::cout << (*iter).second << "\n";
      break;
    }
  }
}

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  int n = 0;
  std::cin >> n;

  for (int i = 0; i < n; i++) {
    printMostExpensive();
  }

  return 0;
}
