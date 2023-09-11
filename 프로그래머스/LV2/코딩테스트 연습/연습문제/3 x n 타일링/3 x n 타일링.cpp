#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    long tiles[5001] = {0,};
    long mod = 1000000007;
    tiles[0] = 1;
    tiles[2] = 3;

    for(int i = 4; i <= n; i += 2)
        tiles[i] = (tiles[i-2]*4 % mod - tiles[i-4] % mod + mod) % mod;

    return tiles[n];
}