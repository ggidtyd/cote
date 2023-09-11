#include <algorithm>
#include <vector>

using namespace std;

bool otherInTent(int i, int j, vector<vector<int>>& data) {
    int startR = min(data[i][0], data[j][0]), endR = max(data[i][0], data[j][0]);
    int startC = min(data[i][1], data[j][1]), endC = max(data[i][1], data[j][1]);
    for (int k = i + 1; k < j; k++) {
        if ((data[k][0] > startR && data[k][0] < endR) && (data[k][1] > startC && data[k][1] < endC))
            return true;
    }
    return false;
}


bool compare(vector<int> arg1, vector<int> arg2) {
    if (arg1[0] == arg2[0])
        return arg1[1] < arg2[1];
    return arg1[0] < arg2[0];
}


// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
int solution(int n, vector<vector<int>> data) {
    int answer = 0;
    sort(data.begin(), data.end(), compare);

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if ((data[i][0] == data[j][0]) || (data[i][1] == data[j][1])) continue;
            if (otherInTent(i, j, data)) continue;
            answer++;
        }
    }
    return answer;
}