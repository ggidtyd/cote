#include <string>
#include <vector>
#include <unordered_set>
#include <unordered_map>
using namespace std;

int solution(vector<int> topping) {
    int answer = 0;
    int ln = 0, rn = 0;
    unordered_set<int> left;
    unordered_map<int, int> right;

    for(int t : topping) {
        if(right.find(t) == right.end()) {
            right[t] = 1;
            rn++;
        }
        else right[t]++;
    }

    for(int i = 0; i < topping.size()-1; i++) {
        if(i != 0 && ln == rn)answer++;

        if(left.find(topping[i]) == left.end())ln++;
        left.insert(topping[i]);

        right[topping[i]]--;
        if(right[topping[i]] == 0)rn--;
    }

    return answer;
}