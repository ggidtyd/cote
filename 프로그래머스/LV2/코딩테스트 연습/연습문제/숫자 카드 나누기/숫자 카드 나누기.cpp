#include <vector>
using namespace std;

int gcd(int a, int b) {
    return b ? gcd(b, a % b) : a;
}

int GcdOfArray(vector<int>& arr, int idx) {
    if (idx == arr.size() - 1) {
        return arr[idx];
    }
    int a = arr[idx];
    int b = GcdOfArray(arr, idx + 1);
    return gcd(a, b);
}

int func(vector<int> arr1, vector<int> arr2) {
    bool f = true;
    int g = GcdOfArray(arr1, 0);
    for(int v : arr2) {
        if(v % g == 0) {
            f = false;
            break;
        }
    }
    return f ? g : 0;
}

int solution(vector<int> arrayA, vector<int> arrayB) {
    return max(func(arrayA, arrayB), func(arrayB, arrayA));
}