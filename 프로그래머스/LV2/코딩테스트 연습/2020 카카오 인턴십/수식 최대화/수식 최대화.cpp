#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(string expression) {
    long long answer = 0;
    string orders[6] = { "*+-", "*-+","+*-", "+-*", "-*+", "-+*" };
    string temp = "";
    vector<long long> nums;
    vector<char> op;

    for (char c : expression) {
        if (c == '+' || c == '*' || c == '-') {
            op.push_back(c);
            nums.push_back(stoi(temp));
            temp = "";
        }
        else temp += c;
    }
    nums.push_back(stoi(temp));

    for (string order : orders) {
        vector<long long> temp_nums = nums;
        vector<char> temp_op = op;
        for (char symbor : order) {
            for (int i = 0; i < temp_op.size(); i++) {
                if (symbor == temp_op[i]) {
                    if (symbor == '*') {
                        temp_nums[i] = temp_nums[i] * temp_nums[i + 1];
                        temp_nums.erase(temp_nums.begin() + i + 1);
                    }
                    else if (symbor == '+') {
                        temp_nums[i] = temp_nums[i] + temp_nums[i + 1];
                        temp_nums.erase(temp_nums.begin() + i + 1);
                    }
                    else if (symbor == '-') {
                        temp_nums[i] = temp_nums[i] - temp_nums[i + 1];
                        temp_nums.erase(temp_nums.begin() + i + 1);
                    }
                    temp_op.erase(temp_op.begin() + i--);
                }
            }
        }
        answer = max(answer, abs(temp_nums[0]));
    }
    return answer;
}