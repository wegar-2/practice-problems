class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int next_valid = 0;
        for (size_t i = 0; i < nums.size(); ++i) {
            if (nums[i] != val) {
                nums[next_valid] = nums[i];
                next_valid += 1;
            }
        }
        return next_valid;
    }
};
