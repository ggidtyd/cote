#include <string>
#include <vector>

using namespace std;

int solution(string name) {
    int answer = 0;
    int name_len = name.length();
    int min_move = name_len - 1;
    int idx = 0;

    for(int i = 0; i < name_len; i++) {
        answer += min(name[i] - 'A', 'Z' + 1 - name[i]);
        idx = i + 1;

        while (idx < name_len && name[idx] == 'A')
            idx++;

        min_move = min(min_move, i * 2 + name_len - idx);
        min_move = min(min_move, (name_len - idx) * 2 + i);
    }
    return answer + min_move;
}