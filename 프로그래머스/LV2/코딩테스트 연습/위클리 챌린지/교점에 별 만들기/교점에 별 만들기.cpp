#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

vector<string> solution(vector<vector<int>> line) {
    vector<string> answer;
    vector<long long int> xs, ys;
    int line_len = line.size();
    int row, col;
    long long int min_x, max_x, min_y, max_y;
    double x, y, xn, yn, d;

    for (int i = 0; i < line_len; i++) {
        for (int j = i+1; j < line_len; j++) {
            d = (double)((long long int)line[i][0] * (long long int)line[j][1]) - (double)((long long int)line[i][1] * (long long int)line[j][0]);
            if (!d)continue;
            xn = (double)((long long int)line[i][1] * (long long int)line[j][2]) - (double)((long long int)line[i][2] * (long long int)line[j][1]);
            yn = (double)((long long int)line[i][2] * (long long int)line[j][0]) - (double)((long long int)line[i][0] * (long long int)line[j][2]);
            x = xn / d;
            y = yn / d;
            if ((x - floor(x) == 0) && (y - floor(y) == 0)) {
                xs.push_back(floor(x));
                ys.push_back(floor(y));
            }
        }
    }

    min_x = *min_element(xs.begin(), xs.end());
    max_x = *max_element(xs.begin(), xs.end());
    min_y = *min_element(ys.begin(), ys.end());
    max_y = *max_element(ys.begin(), ys.end());
    for (int i = 0; i < xs.size(); i++)xs[i] -= min_x;
    for (int i = 0; i < ys.size(); i++)ys[i] = max_y - ys[i];
    row = max_y - (min_y - 1);
    col = max_x - (min_x - 1);

    for (int r = 0; r < row; r++) {
        answer.push_back("");
        for (int c = 0; c < col; c++)answer[r] += '.';
    }
    for (int i = 0; i < xs.size(); i++)answer[ys[i]][xs[i]] = '*';
    return answer;
}