#include <string>
#include <vector>
#include <cmath>
#include <numeric>
using namespace std;

long long solution(int k, int d) {
    long long answer = 0;
    vector<int> xs,ys;

    for(int a = 0; a <= d/k; a++)xs.push_back(a*k);
    for(int x : xs)ys.push_back((int)(sqrt(pow(d,2) - pow(x,2)) / k) + 1);

    return accumulate(ys.begin(), ys.end(), 0LL);
}