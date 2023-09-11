#include <string>
#include <vector>
#include <sstream>
#include <iostream>
using namespace std;

class MusicInfo {
public:
    int start_time;
    int play_time;
    int melody_len;
    string melody;
    string title;

public:
    MusicInfo(string _title, int _start_time = 0, int _play_time = 0, int _melody_len = -1, string _melody = "");
};

MusicInfo::MusicInfo(string _title, int _start_time, int _play_time, int _melody_len, string _melody) {
    title = _title;
    start_time = _start_time;
    play_time = _play_time;
    melody_len = _melody_len;
    melody = _melody;
}

vector<string> split(string str, char c) {
    istringstream iss(str);
    string buffer;

    vector<string> result;

    while (getline(iss, buffer, c))
        result.push_back(buffer);

    return result;
}

void replace_sharp(string& m) {
    while (m.find("C#") != string::npos)m.replace(m.find("C#"), 2, "H");
    while (m.find("D#") != string::npos)m.replace(m.find("D#"), 2, "I");
    while (m.find("F#") != string::npos)m.replace(m.find("F#"), 2, "J");
    while (m.find("G#") != string::npos)m.replace(m.find("G#"), 2, "K");
    while (m.find("A#") != string::npos)m.replace(m.find("A#"), 2, "L");
}

string solution(string m, vector<string> musicinfos) {
    MusicInfo answer = MusicInfo("(None)");
    vector<MusicInfo> music_infos;

    replace_sharp(m);

    for (string info : musicinfos) {
        vector<string> datas = split(info, ',');
        string start_time_str = datas[0], end_time_str = datas[1], title = datas[2], melody = datas[3], origin;
        vector<string> start_hm = split(start_time_str, ':'), end_hm = split(end_time_str, ':');
        int start_time_int = stol(start_hm[0]) * 60 + stol(start_hm[1]), end_time_int = stol(end_hm[0]) * 60 + stol(end_hm[1]);
        int play_time = end_time_int - start_time_int, origin_length;

        replace_sharp(melody);

        origin = melody;
        melody = "";
        origin_length = origin.length();

        for (int i = 0; i < play_time / origin_length; i++) melody.append(origin);
        melody += origin.substr(0, play_time % origin_length);

        music_infos.push_back(MusicInfo(title, start_time_int, play_time, melody.length(), melody));
    }

    for (MusicInfo info : music_infos) {
        if (info.melody.find(m) != string::npos) {
            if (info.melody_len > answer.melody_len) answer = info;
            else if ((info.melody_len == answer.melody_len) && (info.start_time < answer.start_time)) answer = info;
        }
    }

    return answer.title;
}