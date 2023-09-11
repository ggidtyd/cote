using namespace std;

int solution(int n) {
    int answer = 0;
    int a = 1, b = 2;

    for (int i = 3; i <= n; i++) {
        answer = (a + b) % 1000000007;
        a = b;
        b = answer;
    }
    return answer;
}