#include <string>

using namespace std;

class Solution {
public:
    int compress(vector<char>& chars) {
        int write = 0;

        char curr_char;
        int cnt_curr_char = 0;

        for (size_t i = 0; i < chars.size(); ++i) {
            if (i == 0) {
                curr_char = chars[i];
                cnt_curr_char = 1;
                if (chars.size() == 1) { return 1; }
            } else {
                if (chars[i] != curr_char) {
                    chars[write++] = curr_char;
                    if (cnt_curr_char > 1) {
                        for (const char& c : to_string(cnt_curr_char)) { chars[write++] = c; }
                    }
                    if (i == chars.size() - 1) { 
                        chars[write++] = chars[i]; 
                    } else {
                        curr_char = chars[i];
                        cnt_curr_char = 1;
                    }

                } else {
                    cnt_curr_char++;
                    if (i == chars.size() - 1) {
                        chars[write++] = curr_char;
                        for (const char& c : to_string(cnt_curr_char)) { chars[write++] = c; }
                    }
                }
            }
        }

        return write;
    }
};
