#include<vector>
#include<deque>
#include <iostream>
#define Point pair<int,int>
using namespace std;

class NODE {
public:
    Point point;
    int level;

    NODE();
    NODE(Point p, int l) {
        point = p;
        level = l;
    }
};

vector<Point> get_connections(vector<vector<int>>& maps, Point cp, vector<Point>& move, int N, int M) {
    vector<Point> connections;
    int next_r, next_c;
    for (Point m : move) {
        next_r = cp.first + m.first;
        next_c = cp.second + m.second;
        if (next_r < 0 || next_r >= N || next_c < 0 || next_c >= M)continue;
        if (!maps[next_r][next_c])continue;
        connections.push_back(Point(next_r, next_c));
    }
    return connections;
}

int solution(vector<vector<int> > maps) {
    int answer = -1, level = 1;
    int N = maps.size(), M = maps[0].size();
    Point start = Point(0, 0), end = Point(N - 1, M - 1), cur_point;
    vector<Point> move = { {1,0}, {-1,0}, {0,-1}, {0,1} };
    vector<Point> connections;
    NODE first = NODE(start, 1);
    deque<NODE> q = { first };
    maps[0][0] = 0;

    while (!q.empty()) {
        cur_point = q.front().point;
        level = q.front().level;
        q.pop_front();

        if (cur_point == end) {
            answer = level;
            break;
        }

        connections = get_connections(maps, cur_point, move, N, M);
        for (Point con : connections) {
            q.push_back(NODE(con, level + 1));
            maps[con.first][con.second] = 0;
        }
    }
    return answer;
}