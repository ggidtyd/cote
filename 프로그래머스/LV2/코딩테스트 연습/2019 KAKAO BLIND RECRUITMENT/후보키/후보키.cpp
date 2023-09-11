#include <string>
#include <vector>
#include <algorithm>
#include <set>
using namespace std;

bool duplicate(vector<string> v) {
    for (size_t i = 0; i < v.size(); i++)
        for (size_t j = i + 1; j < v.size(); j++)
            if (v[i] == v[j])return true;
    return false;
}

bool key(string combi, vector<vector<string>>& relation) {
    vector<string> arr;
    string temp;
    for (vector<string> row : relation) {
        temp = "";
        for (char c : combi)
            temp += row[c - '0'];
        arr.push_back(temp);
    }
    return !duplicate(arr);
}

vector<string> get_combis(string cols, int i) {
    vector<string> combis;
    vector<bool> v(cols.length() - i, false);
    v.insert(v.end(), i, true);
    do {
        string temp = "";
        for (size_t j = 0; j < cols.length(); j++)
            if (v[j])temp += cols[j];
        combis.push_back(temp);
    } while (next_permutation(v.begin(), v.end()));
    return combis;
}

bool doesnt_have_ck(string col_combi, set<string>& candidate_key) {
    vector<string> combis;

    for (size_t i = 1; i <= col_combi.length(); i++) {
        combis = get_combis(col_combi, i);
        for (string combi : combis)
            if (candidate_key.find(combi) != candidate_key.end())
                return false;
    }
    return true;
}

void append_ck(string cols, set<string>& ck, vector<vector<string>>& relation) {
    vector<string> combis;
    for (size_t k = 2; k <= cols.length(); k++) {
        combis = get_combis(cols, k);
        for (string combi : combis) {
            if (doesnt_have_ck(combi, ck) && key(combi, relation))ck.insert(combi);
        }
    }
}

int solution(vector<vector<string>> relation) {
    string duplicate_cols = "";
    set<string> candidate_key;
    vector<vector<string>> cols;
    vector<string> temp;

    for (size_t i = 0; i < relation[0].size(); i++) {
        temp.clear();
        for (vector<string> t : relation)temp.push_back(t[i]);
        cols.push_back(temp);
    }

    for (size_t i = 0; i < relation[0].size(); i++) {
        if (duplicate(cols[i]))duplicate_cols += to_string(i);
        else candidate_key.insert(to_string(i));
    }

    append_ck(duplicate_cols, candidate_key, relation);
    return candidate_key.size();
}