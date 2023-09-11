#include <string>
#include <vector>
#include <cmath>
using namespace std;

vector<long long> solution(vector<long long> numbers) {
    vector<long long> answer;
    long long b, temp;
    for(long long n : numbers) {
        b = 1;
        temp = n;
        while (true) {
            if(!(temp & 1))break;
            temp >>= 1;
            b <<= 1;
        }
        answer.push_back(n + b - (b>>1));  
    }
    return answer;
}