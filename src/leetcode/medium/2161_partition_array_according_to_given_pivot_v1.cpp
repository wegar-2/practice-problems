/* linguistically ugly implementation */

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
        for (auto x : lt) { out.push_back(x); }
        for (auto x : et) { out.push_back(x); }
        for (auto x : gt) { out.push_back(x); }

        return out;
    }
};
