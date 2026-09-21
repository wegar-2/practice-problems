class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int out = 0;
        for (auto x : nums) { out ^= x; }
        return out;
    }
};
