#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    sort(citations.begin(), citations.end());
    int cl = citations.size();
    int h = 0;

    for(int i = 0; i < cl; i++) {
        if(citations[i] >= cl-i) {
            h = cl-i;
            break;
        }
    }
    return h;
}