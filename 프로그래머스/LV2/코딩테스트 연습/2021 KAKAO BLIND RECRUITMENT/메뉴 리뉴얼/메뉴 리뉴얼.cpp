#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
using namespace std;

void courses_that_can_be_made_in_each_order(int j, string order, string course, int course_menu_num, unordered_set<string>& courses) {
    if (course.length() == course_menu_num) {
        sort(course.begin(), course.end());
        courses.insert(course);
        return;
    }

    for (int i = j; i < order.length(); i++)
        courses_that_can_be_made_in_each_order(i + 1, order, course + order[i], course_menu_num, courses);
}

int include_check(string course, string order) {
    int ret = 1;
    vector<bool> in(course.length(), false);

    for (int i = 0; i < course.length(); i++)
        if (order.find(course[i]) != string::npos)in[i] = true;

    for (bool b : in)ret *= b;

    return ret;
}

vector<string> solution(vector<string> orders, vector<int> course) {
    vector<string> answer;
    unordered_set<string> courses;
    unordered_map<int, vector<pair<string, int>>> map;


    for (int course_menu_num : course)
        for (string order : orders)
            courses_that_can_be_made_in_each_order(0, order, "", course_menu_num, courses);

    for (string course : courses) {
        vector<pair<string, int>> vec;
        int ordered_num = 0;
        for (string order : orders)
            ordered_num += include_check(course, order);

        if (ordered_num < 2)continue;

        if (map.find(course.length()) == map.end()) {
            vec = { make_pair(course, ordered_num) };
            map.insert({ course.length(), vec });
        }
        else if (ordered_num > map[course.length()][0].second) {
            vec = { make_pair(course, ordered_num) };
            map[course.length()] = vec;
        }
        else if (ordered_num == map[course.length()][0].second)
            map[course.length()].push_back(make_pair(course, ordered_num));
    }

    for (auto it : map)
        for (pair<string, int> p : it.second)
            answer.push_back(p.first);

    sort(answer.begin(), answer.end());
    return answer;
}