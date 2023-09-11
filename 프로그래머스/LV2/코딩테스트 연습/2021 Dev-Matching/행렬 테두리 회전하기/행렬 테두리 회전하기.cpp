#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    vector<vector<int>> origin;

    for (int r = 0; r <= rows; r++) {
        vector<int> v(columns + 1, 0);
        origin.push_back(v);
    }

    for (int r = 1; r <= rows; r++)
        for (int c = 1; c <= columns; c++)
            origin[r][c] = ((r - 1) * columns + c);

    for (vector<int> query : queries) {
        int x1 = query[0], y1 = query[1];
        int x2 = query[2], y2 = query[3];
        vector<vector<int>> temp_map = origin;
        vector<int> moved_values;

        for (int c = y1; c < y2; c++) {
            origin[x1][c + 1] = temp_map[x1][c];
            origin[x2][c] = temp_map[x2][c + 1];
            moved_values.push_back(temp_map[x1][c]);
            moved_values.push_back(temp_map[x2][c + 1]);
        }
        for (int r = x1; r < x2; r++) {
            origin[r + 1][y2] = temp_map[r][y2];
            origin[r][y1] = temp_map[r + 1][y1];
            moved_values.push_back(temp_map[r][y2]);
            moved_values.push_back(temp_map[r + 1][y1]);
        }
        answer.push_back(*min_element(moved_values.begin(), moved_values.end()));
    }
    return answer;
}