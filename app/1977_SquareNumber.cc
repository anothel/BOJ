#include <iostream>
#include <vector>

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  int M, N;
  std::cin >> M >> N;

  std::vector<int> vBucket;
  for (int i = 1; i <= 100; i++) {
    vBucket.push_back(i * i);
  }

  int nStart = -1, nEnd = -1;
  for (int i = 0; i < vBucket.size(); i++) {
    if (nStart < 0 && M <= vBucket[i] && vBucket[i] <= N) {
      nStart = i;
    }
    if (N < vBucket[i]) {
      nEnd = i;
      break;
    }
  }

  if (N == 10000) {
    nEnd = vBucket.size();
  }

  if (-1 < nStart) {
    int nSum = 0;
    for (int i = nStart; i < nEnd; i++) {
      nSum += vBucket[i];
    }
    std::cout << nSum << "\n";
    std::cout << vBucket[nStart] << "\n";
  } else {
    std::cout << -1 << "\n";
  }

  return 0;
}
