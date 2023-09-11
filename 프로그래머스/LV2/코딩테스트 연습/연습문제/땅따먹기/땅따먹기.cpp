#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int get_max_excluding_current_col_in_up_row(int cur_col, vector<int>& up_row) {
    int max_in_up_row = 0;
    for (int c = 0; c < 4; c++) {
        if (c == cur_col)continue;
        if (up_row[c] > max_in_up_row)max_in_up_row = up_row[c];
    }
    return max_in_up_row;
}

int solution(vector<vector<int>> land) {
    int answer = 0;
    int row = land.size();

    for (int r = 1; r < row; r++) {
        for (int c = 0; c < 4; c++)land[r][c] += get_max_excluding_current_col_in_up_row(c, land[r-1]);
    }

    return land[row - 1][max_element(land[row - 1].begin(), land[row - 1].end()) - land[row - 1].begin()];
}