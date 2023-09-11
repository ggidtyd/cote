#include <string>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class P {
public:
    int r = 0;
    int c = 0;
    int pdi = 0;
    int cost = 0;

    P(int _r, int _c, int _pdi, int _cost) {
        this->r = _r;
        this->c = _c;
        this->pdi = _pdi;
        this->cost = _cost;
    }
};

int solution(vector<vector<int>> board) {
    int N = board.size();
    vector<vector<vector<int>>> locCost;
    for (int r = 0; r < N; r++) {
        vector<vector<int>> row;
        for (int c = 0; c < N; c++) {
            vector<int> temp(4, 25 * 25 * 500);
            row.push_back(temp);
        }
        locCost.push_back(row);
    }

    vector<vector<int>> ds = { {1, 0}, {0, 1}, {-1, 0}, {0, -1} };
    queue<P> q;
    q.push(P(0, 0, 0, 0));
    q.push(P(0, 0, 1, 0));

    while (!q.empty()) {
        P p = q.front();
        q.pop();

        for (int di = 0; di < 4; di++) {
            int nextR = p.r + ds[di][0];
            int nextC = p.c + ds[di][1];
            if (nextR < 0 || nextR >= N || nextC < 0 || nextC >= N) continue;
            if (board[nextR][nextC] == 1) continue;

            int newCost = di == p.pdi ? p.cost + 100 : p.cost + 600;

            if (newCost < locCost[nextR][nextC][di]) {
                locCost[nextR][nextC][di] = newCost;
                q.push(P(nextR, nextC, di, newCost));
            }
        }
    }
    return *min_element(locCost[N-1][N-1].begin(), locCost[N - 1][N - 1].end());;
}