#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {

        unordered_map<char, int> um_s;
        unordered_map<char, int> um_t;

        if (s.length() != t.length()) { return false; }
        for (char& c : s) { um_s[c]++; }
        for (char& c : t) { um_t[c]++; }

        return um_s == um_t;
    }
};
