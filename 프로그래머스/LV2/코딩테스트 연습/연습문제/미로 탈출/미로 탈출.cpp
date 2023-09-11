#include <string>
#include <vector>
#include <queue>
#include <iostream>
using namespace std;
typedef pair<int, int> point;
typedef pair<point, int> NODE;

struct sel {
    point start;
    point end;
    point lever;
}typedef SEL;

int bfs(vector<string>& maps, point start, point end, int R, int C) {
    vector<vector<int>> move = { {1, 0}, {-1, 0}, {0, 1}, {0, -1} };
    vector<vector<int>> visited;
    for (int r = 0; r < R; r++) {
        vector<int> row(C, false);
        visited.push_back(row);
    }
    queue<NODE> q;
    visited[start.first][start.second] = true;
    q.push(NODE(start, 0));

    while (!q.empty()) {
        NODE curNode = q.front();
        q.pop();
        point cur = curNode.first;
        int time = curNode.second;
        
        if (cur == end)
            return time;

        for (vector<int> m : move) {
            int nextR = cur.first + m[0], nextC = cur.second + m[1];
            if (nextR < 0 || nextR >= R || nextC < 0 || nextC >= C) continue;
            if (maps[nextR][nextC] == 'X') continue;
            if (visited[nextR][nextC]) continue;
            visited[nextR][nextC] = true;
            q.push(NODE(point(nextR, nextC), time+1));
        }
    }
    return -1;
}

SEL getStartEndLever(vector<string>& maps, int R, int C) { 
    point notFounded = point(-1, -1);
    SEL sel = { notFounded, notFounded, notFounded };

    for (int r = 0; r < R; r++) {
        for (int c = 0; c < C; c++) {
            if (sel.start != notFounded && sel.end != notFounded && sel.lever != notFounded)
                return sel;
            
            if (maps[r][c] == 'S') sel.start = point(r, c);
            else if (maps[r][c] == 'E') sel.end = point(r, c);
            else if (maps[r][c] == 'L') sel.lever = point(r, c);
        }
    }
    return sel;
}

int solution(vector<string> maps) {
    int R = maps.size(), C = maps[0].length();
    SEL sel = getStartEndLever(maps, R, C);

    int toL = bfs(maps, sel.start, sel.lever, R, C);
    if (toL == -1) return -1;
    int toE = bfs(maps, sel.lever, sel.end, R, C);
    if (toE == -1) return -1;

    return toL + toE;
}