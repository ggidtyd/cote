#include <vector>
#define point pair<int,int>
using namespace std;

int cnt = 0;

void go(vector<vector<bool>>& check, vector<vector<int>>& picture, vector<point>& d, int r, int c, int m, int n, int area) {
    int next_r = 0;
    int next_c = 0;
    for (point p : d) {
        next_r = r + p.first;
        next_c = c + p.second;
        if (next_r < 0 || next_r >= m || next_c < 0 || next_c >= n)continue;
        if (check[next_r][next_c])continue;
        if (!picture[next_r][next_c])continue;
        if (picture[next_r][next_c] != area)continue;

        check[next_r][next_c] = true;
        cnt++;
        go(check, picture, d, next_r, next_c, m, n, area);
    }
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    vector<point> d = { point(0,1), point(0,-1), point(-1,0), point(1,0), };
    vector<vector<bool>> check;
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    cnt = 0;

    for (int i = 0; i < m; i++) {
        vector<bool> temp;
        for (int j = 0; j < n; j++)
            temp.push_back(false);
        check.push_back(temp);
    }

    for (int r = 0; r < m; r++) {
        for (int c = 0; c < n; c++) {
            if (check[r][c])continue;
            if (!picture[r][c])continue;
            cnt = 0;
            go(check, picture, d, r, c, m, n, picture[r][c]);
            max_size_of_one_area = max(max_size_of_one_area, cnt);
            number_of_area++;
        }
    }

    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}