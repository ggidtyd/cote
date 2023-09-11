#include <string>
#include <vector>
#define point pair<int, int>
using namespace std;

bool same2x2(int r, int c, vector<string>& board) {
    if(board[r][c] == 0)return false;
    if(board[r][c] == board[r+1][c] == board[r][c+1] == board[r+1][c+1])
        return true;
    return false;
}

vector<point> find_core_points(int m, int n, vector<string>& board) {
    vector<point> core_points;
    
    for(int r = 0; r <= m-1; r++) {
        for(int c = 0; c <= n-1; c++) {
            if(same2x2(r,c,board))core_points.push_back(make_pair(r,c));
        }
    }
    return core_points;
}

void down(int r, int c, vector<string>& board) {
    for(int rr = 0; rr < r; rr++) {
        board[r-rr][c] = board[r-rr-1][c];
        board[r-rr-1][c] = 0;
    }
}

int count_and_down(int m, int n, vector<string>& board) {
    int cnt = 0;
    for(int r = 0; r < m; r++) {
        for(int c = 0; c < n; c++) {
            if(board[r][c] == -1) {
                cnt++;
                board[r][c] = 0;
                down(r,c,board);
            }
        }
    }
    return cnt;
}

void set2x2m1(vector<point>& cps, vector<string>& board) {
    for(point pt : cps) {
        board[pt.first][pt.second] = -1;
        board[pt.first+1][pt.second] = -1;
        board[pt.first][pt.second+1] = -1;
        board[pt.first+1][pt.second+1] = -1;
    }
}

int solution(int m, int n, vector<string> board) {
    int answer = 0;
    vector<point> core_points;
    int cur_core_point_num = 0;

    while (true) {
        core_points = find_core_points(m,n,board);
        if(core_points.size() == 0)break;

        set2x2m1(core_points,board);
        answer += count_and_down(m,n,board);
        cur_core_point_num = 0;
        core_points.clear();
    }
    return answer;
}