#include <string>
#include <vector>
#include <sstream>
#include <map>
#define ss pair<string, string>
using namespace std;

vector<string> split(string str, char Delimiter) {
    istringstream iss(str);
    string buffer;

    vector<string> result;

    while (getline(iss, buffer, Delimiter))
        result.push_back(buffer);

    return result;
}

vector<string> solution(vector<string> record) {
    vector<string> answer, splitted;
    vector<ss> enter_leave;
    map<string, string> uid_name_map;
    string action, uid, name;

    for (string rec : record) {
        if (rec[0] == 'L') {
            splitted = split(rec, ' ');
            action = splitted[0];
            uid = splitted[1];
            enter_leave.push_back(make_pair(action, uid));
            continue;
        }

        splitted = split(rec, ' ');
        action = splitted[0];
        uid = splitted[1];
        name = splitted[2];
        if (action == "Change")uid_name_map[uid] = name;
        else if (action == "Enter") {
            uid_name_map[uid] = name;
            enter_leave.push_back(make_pair(action, uid));
        }
    }

    for (ss el : enter_leave) {
        action = el.first;
        uid = el.second;
        if (action == "Enter")answer.push_back(uid_name_map[uid] + "님이 들어왔습니다.");
        else answer.push_back(uid_name_map[uid] + "님이 나갔습니다.");
    }
    return answer;
}