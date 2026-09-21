class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> vec;
        for (auto op : operations) {
            if (op == "C") {
                vec.pop_back();
            } else if (op == "D") {
                vec.push_back(2 * vec[vec.size() - 1]);
            } else if (op == "+") {
                int vec_m1 = vec[vec.size() - 1];
                int vec_m2 = vec[vec.size() - 2];
                vec.push_back(vec_m1 + vec_m2);
            } else {
                vec.push_back(stoi(op));
            }
        }

        int out = 0;
        for (auto x : vec) { out += x; }
        return out;
    }
};
