class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {

        unordered_map<int, pair<int, int>> requires_number;
        vector<int> out;

        for (size_t i = 0; i < nums.size(); ++i) {
            if (requires_number.contains(nums[i])) {
                auto p = requires_number[nums[i]];
                out.push_back(min(int(i), p.first));
                out.push_back(max(int(i), p.first));
                return out;
            } else {
                requires_number[target - nums[i]] = make_pair(i, nums[i]);
            }
        }
    }
};
