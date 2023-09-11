#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <cctype>
#include <iterator>
using namespace std;

int solution(string str1, string str2) {
    int numerator = 0;
    int denominator = 0;
    double JAB;
    vector<string> A, B, intersection, uni;

    transform(str1.begin(), str1.end(), str1.begin(), ::toupper);
    transform(str2.begin(), str2.end(), str2.begin(), ::toupper);
    for (int i = 0; i <= str1.length() - 2; i++)if(isalpha(str1[i]) && isalpha(str1[i+1]))A.push_back(str1.substr(i, 2));
    for (int i = 0; i <= str2.length() - 2; i++)if(isalpha(str2[i]) && isalpha(str2[i+1]))B.push_back(str2.substr(i, 2));
    
    set<string> AS(A.begin(), A.end());
    set<string> BS(B.begin(), B.end());

    set_intersection(AS.begin(), AS.end(),BS.begin(), BS.end(),back_inserter(intersection));
    set_union(AS.begin(), AS.end(),BS.begin(), BS.end(),back_inserter(uni));

    for (string ab : intersection)numerator += min(count(A.begin(), A.end(), ab), count(B.begin(), B.end(), ab));
    for (string ab : uni)denominator += max(count(A.begin(), A.end(), ab), count(B.begin(), B.end(), ab));

    JAB = numerator == 0 && denominator == 0 ? 1 : (double)numerator / (double)denominator;
    return (int)(JAB * 65536);
}