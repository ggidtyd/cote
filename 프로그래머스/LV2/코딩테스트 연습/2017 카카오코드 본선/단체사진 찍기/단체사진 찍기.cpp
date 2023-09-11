#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int solution(int n, vector<string> data);
void cal(int n,vector<string> v);
bool condition_satisfaction_check(string condition);

int cnt = 0;
string s = "ACFJMNRT";

bool condition_satisfaction_check(string condition) {
	char l = condition[0];
	char r = condition[2];
	char c = condition[3];
	int distance = condition[4] - '0';

	int left_idx = find(s.begin(), s.end(), l) - s.begin();
	int right_idx = find(s.begin(), s.end(), r) - s.begin();
	int bi = 0;
	int si = 0;

	if (right_idx > left_idx) {
		bi = right_idx;
		si = left_idx;
	}
	else if (right_idx < left_idx) {
		bi = left_idx;
		si = right_idx;
	}

	if (c == '>' && bi - 1 - si <= distance)
		return false;
	else if (c == '<' && bi - 1 - si >= distance)
		return false;
	else if (c == '=' && bi - 1 - si != distance)
		return false;

	return true;
}

void cal(int n, vector<string> v) {
	bool flag = true;
	do {
		flag = true;
		for (int i = 0; i < n; i++) {
			if (!condition_satisfaction_check(v[i])) {
				flag = false;
				break;
			}
		}
		if (flag)
			cnt++;
	} while (next_permutation(s.begin(), s.end()));
	return;
}

int solution(int n, vector<string> data) {
	cnt = 0;

	cal(n, data);

	return cnt;
}