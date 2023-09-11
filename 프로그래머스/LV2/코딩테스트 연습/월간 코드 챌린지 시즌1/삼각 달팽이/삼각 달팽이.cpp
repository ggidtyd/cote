#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n) {
    vector<int> answer, temp;
    vector<vector<int>> map;
    int i = 1, direction = 0, r_start = 0, c_start = 0;
    for(int i = 0; i < n; i++) {
        temp.clear();
        for(int i = 0; i < n; i++)temp.push_back(0);
        map.push_back(temp);
    }

    for(int l = n; l >= 1; l--) {
        if(direction % 3 == 0) {
            for(int r = 0; r < l; r++) {
                map[r_start+r][c_start] = i++;
            }
            c_start++;
        }
        else if(direction % 3 == 1) {
            for(int c = 0; c < l; c++) {
                map[r_start+l][c_start+c] = i++;
            }
            r_start++;            
        }
        else if(direction % 3 == 2) {
            for(int di = 1; di <= l; di++) {
                map[r_start+l-di][c_start+l-di] = i++;
            }
            r_start++;
        }
        direction++;
    }

    for(vector<int> row : map) {
        for(int i : row) {
            if(i == 0)break;
            answer.push_back(i);
        }
    }
    return answer;
}