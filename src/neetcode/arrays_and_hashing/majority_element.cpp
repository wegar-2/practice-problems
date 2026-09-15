class Solution {
// Using Boyer-Moore voting algorithm
public:
    int majorityElement(vector<int>& nums) {

        int candidate;
        int candidate_count = 0;

        for (size_t i = 0; i < nums.size(); ++i) {
            if (i == 0) {
                candidate = nums[0];
                candidate_count = 1;
            } else {
                if (candidate == nums[i]) {
                    candidate_count += 1;
                } else {
                    if (candidate_count == 0) {
                        candidate_count = 1;
                        candidate = nums[i];
                    } else {
                        candidate_count -= 1;
                    }
                }
            }
        }

        return candidate;
    }
};
