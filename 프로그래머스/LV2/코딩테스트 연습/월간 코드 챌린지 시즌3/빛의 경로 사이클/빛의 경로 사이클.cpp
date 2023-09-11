#include <string>
#include <vector>
#include <algorithm>
#include <set>
#define d pair<int, int>

using namespace std;

vector<vector<set<d>>> d_record;
vector<d> directions = { d(-1,0), d(0,1), d(1,0), d(0,-1) };
vector<int> path_lens;
d start_d, start_rc;
int R, C, directions_len = directions.size();

void go(int r, int c, int di, d start_rc, d start_d, int path_len, vector<string>& grid) {
    if (grid[r][c] == 'L')di = ((di + 1) + directions_len) % directions_len;
    else if (grid[r][c] == 'R')di = ((di - 1) + directions_len) % directions_len;

    if (d_record[r][c].find(directions[di]) != d_record[r][c].end())return;
    else d_record[r][c].insert(directions[di]);

    if (d(r, c) == start_rc && directions[di] == start_d) {
        path_lens.push_back(path_len);
        return;
    }

    int next_r = ((r + directions[di].second) + R) % R;
    int next_c = ((c + directions[di].first) + C) % C;
    go(next_r, next_c, di, start_rc, start_d, path_len + 1, grid);
}

vector<int> solution(vector<string> grid) {
    vector<set<d>> temp;
    R = grid.size();
    C = grid[0].length();
    int path_len = 1;

    for (int r = 0; r < R; r++) {
        temp.clear();
        for (int c = 0; c < C; c++) {
            set<d> s;
            temp.push_back(s);
        }
        d_record.push_back(temp);
    }

    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            for (int di = 0; di < directions_len; di++) {
                if (d_record[r][c].find(directions[di]) != d_record[r][c].end())continue;
                start_rc = d(r, c);
                start_d = d(directions[di].first, directions[di].second);
                int next_r = ((r + directions[di].second) + R) % R;
                int next_c = ((c + directions[di].first) + C) % C;
                go(next_r, next_c, di, start_rc, start_d, path_len, grid);
            }
        }
    }
    sort(path_lens.begin(), path_lens.end());
    return path_lens;
}