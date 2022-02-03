#include <iostream>
#include <vector>

enum : int { MAX_NUM = 7 };

static int N(0), M(0);
static std::vector<int> vAnswer;
static bool bVisited[MAX_NUM];

void dfs(const int& count) {
    if (M == count) {
        for (int i = 0; i < M; i++) std::cout << vAnswer[i] << " ";
        std::cout << "\n";

        return;
    }

    for (int i = 0; i < N; i++) {
        vAnswer.push_back(i + 1);
        dfs(count + 1);
        vAnswer.pop_back();
    }
    return;
}

int main() {
    std::cout.tie(NULL);
    std::cin.tie(NULL);
    std::ios_base::sync_with_stdio(false);

    std::cin >> N >> M;

    dfs(0);

    return 0;
}
