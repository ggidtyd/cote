#include <string>
#include <vector>

using namespace std;

vector<int> get_hail_progression(int k) {
    vector<int> hail_progression = {k};
    while (k != 1) {
        if(k % 2)k = k * 3 + 1;
        else k /= 2;
        hail_progression.push_back(k);
    }
    return hail_progression;
}

vector<double> solution(int k, vector<vector<int>> ranges) {
    vector<double> result;
    vector<int> hail_progression = get_hail_progression(k);
    int hail_progression_end = hail_progression.size()-1;
    int left, right;
    double temp;

    for(vector<int> range : ranges) {
        left = range[0];
        right = hail_progression_end + range[1];
        temp = left <= right ? 0 : -1;
        for(int i = left; i < right; i++) {
            temp += min(hail_progression[i], hail_progression[i+1]);
            temp += (double)abs(hail_progression[i]-hail_progression[i+1])/2;
        }
        result.push_back(temp);
    }   
    return result;
}