long long solution(int n) {
    long long answer = 0, a = 2, b = 3;
    if(n <= 3)return n;
    
    for(int i = 4; i <= n; i++) {
        answer = (a+b)%1234567;
        a = b;
        b = answer;
    }
    return answer;
}