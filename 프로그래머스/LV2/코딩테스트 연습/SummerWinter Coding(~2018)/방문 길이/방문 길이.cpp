#include <string>
#include <set>
#include <map>
#define point pair<int,int>
using namespace std;

int solution(string dirs) {
    int answer = 0;
    int cur_x = 0, cur_y = 0, next_x = 0, next_y = 0;
    set<string> ways;
    string way, reverse_way;

    map<char, point> move = { make_pair('U', point(0,1)),make_pair('R', point(1,0)),
    make_pair('D', point(0,-1)), make_pair('L', point(-1,0)) };

    for (char d : dirs) {

        next_x = cur_x + move[d].first;
        next_y = cur_y + move[d].second;

        if (next_x < -5 || next_x > 5 || next_y < -5 || next_y > 5)continue;

        way = to_string(cur_x) + to_string(cur_y) + to_string(next_x) + to_string(next_y);
        reverse_way = to_string(next_x) + to_string(next_y) + to_string(cur_x) + to_string(cur_y);
        if (ways.find(way) == ways.end() && ways.find(reverse_way) == ways.end()) {
            answer++;
            ways.insert(way);
        }
        cur_x = next_x;
        cur_y = next_y;
    }
    return answer;
}