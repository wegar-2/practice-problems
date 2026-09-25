
class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector<int> lt;
        vector<int> et;
        vector<int> gt;

        for (auto num : nums) {
            if (num < pivot) lt.push_back(num);
            else if (num == pivot) { et.push_back(num); }
            else { gt.push_back(num); }
        }

        vector<int> out;
        out.reserve(nums.size());
        out.insert(out.begin(), lt.begin(), lt.end());
        out.insert(out.end(), et.begin(), et.end());
        out.insert(out.end(), gt.begin(), gt.end());
        return out;
    }
};
