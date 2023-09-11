#include <vector>
#include <set>
using namespace std;

int solution(vector<int> elements) {
    set<int> answer;

    int elements_len = elements.size();
    vector<int> sums(elements_len, 0);

    for(int i = 0; i < elements_len - 1; i++) {
        for(int j = 0; j < elements_len; j++)
            sums[j] += elements[(i+j) % elements_len];
        
        for(int s : sums)
            answer.insert(s);
    }

    return answer.size() + 1;
}