#include <iostream>
#include <vector>

static int N = 0;
static int a = 0, i = 0;

int main() {
  std::cout.tie(NULL);
  std::cin.tie(NULL);
  std::ios_base::sync_with_stdio(false);

  int dp[41] = {0, 1, 1};

  for (i = 3; i < 41; i++) dp[i] = dp[i - 1] + dp[i - 2];

  std::cin >> N;
  for (i = 0; i < N; i++) {
    std::cin >> a;
    switch (a) {
      case 0: {
        std::cout << "1 0\n";
        break;
      }
      case 1: {
        std::cout << "0 1\n";
        break;
      }
      default: {
        std::cout << dp[a - 1] << " " << dp[a] << "\n";
        break;
      }
    }
  }

  return 0;
}
