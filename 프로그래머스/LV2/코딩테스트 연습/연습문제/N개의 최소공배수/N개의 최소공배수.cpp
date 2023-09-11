#include <vector>

using namespace std;

int gcd(int a, int b) {
	return b ? gcd(b, a%b) : a;
}

int solution(vector<int> arr) {
    int answer = 1;
    for(int v : arr)answer = answer * v / gcd(answer, v);
    return answer;
}