#include <string>
#include <vector>
#include <algorithm>
#define d pair<int, int>
using namespace std;

vector<vector<vector<bool>>> d_check;
vector<d> dxy;
int R, C;

int solve(int r, int c, int d_idx, vector<string>& grid) {
    int path_len = 0;
    while (!d_check[r][c][d_idx]) {
        d_check[r][c][d_idx] = true;
        r = ((r + dxy[d_idx].first)+R) % R;
        c = ((c + dxy[d_idx].second)+C) % C;

        if (grid[r][c] == 'L') d_idx = ((d_idx + 1)+4) % 4;
        else if (grid[r][c] == 'R')d_idx = ((d_idx - 1)+4)%4;
        path_len++;
    }
    return path_len;
}

vector<int> solution(vector<string> grid) {
    vector<int> answer;
    vector<vector<bool>> temp;
    dxy = { d(-1,0), d(0,1), d(1,0), d(0,-1) };
    R = grid.size();
    C = grid[0].length();

    for (int i = 0; i < R; i++) {
        temp.clear();
        for (int j = 0; j < C; j++) {
            temp.push_back({ false,false,false,false });
        }
        d_check.push_back(temp);
    }

    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            for (int di = 0; di < dxy.size(); di++)
                if (d_check[r][c][di] == 0)answer.push_back(solve(r, c, di, grid));
        }
    }
    sort(answer.begin(), answer.end());
    return answer;
}