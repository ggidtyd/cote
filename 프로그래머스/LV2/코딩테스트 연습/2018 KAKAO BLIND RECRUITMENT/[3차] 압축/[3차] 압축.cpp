#include <string>
#include <vector>
#include <map>
using namespace std;

vector<int> solution(string msg) {
    vector<int> answer;
    map<string, int> lzw;
    string w, wc, temp;
    int index = 27;
    int msg_len = msg.length();
    int max_len = 1;
    int w_pos = 0, c_pos = 0;
    

    for (char c = 'A'; c <= 'Z'; c++) {
        temp = c;
        lzw.insert(make_pair(temp, c - 64));
    }

    while (w_pos < msg_len) {
        for(int w_len = max_len; w_len > 0; w_len--) {
            c_pos = w_pos + w_len;
            w = msg.substr(w_pos, w_len);
            if (lzw.find(w) != lzw.end()) {
                answer.push_back(lzw.at(w));
                if (c_pos >= msg_len) {
                    w_pos = c_pos;
                    break;
                }
                wc = w + msg[c_pos];
                lzw[wc] = index++;
                w_pos = c_pos;
                if(wc.length() > max_len) max_len = wc.length();
                break;
            }
        }
    }
    return answer;
}