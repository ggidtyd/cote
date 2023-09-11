#include <string>
#include <vector>
#include <sstream>
#include <algorithm>

using namespace std;

vector<string> split(string str, char d) {
    istringstream iss(str);
    string buffer;

    vector<string> result;

    while (getline(iss, buffer, d))
        result.push_back(buffer);

    return result;
}

int toMinutes(string hhmm) {
    vector<string> hm = split(hhmm, ':');
    return stoi(hm[0]) * 60 + stoi(hm[1]);
}

int solution(vector<vector<string>> bookTime) {
    vector<pair<int, int>> bookTimeInt;
    for(int i = 0; i < bookTime.size(); i++)
        bookTimeInt.push_back(make_pair(toMinutes(bookTime[i][0]), toMinutes(bookTime[i][1])));
    

    sort(bookTimeInt.begin(), bookTimeInt.end());
    vector<pair<int, int>> rooms(1, bookTimeInt[0]);
    bool flag;
    
    for(int i = 1; i < bookTimeInt.size(); i++) {
        flag = false;
        for(int j = 0; j < rooms.size(); j++) {
            if(rooms[j].second + 10 <= bookTimeInt[i].first) {
                rooms[j].second = bookTimeInt[i].second;
                flag = true;
                break;
            }
        }
        if(!flag) rooms.push_back(bookTimeInt[i]);
    }

    return rooms.size();
}