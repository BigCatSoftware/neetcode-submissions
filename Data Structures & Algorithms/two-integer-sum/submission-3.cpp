class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> indices{};
        int n = static_cast<int>(nums.size());

        for (int i = 0; i < n; i++) {
            int diff = target - nums[i];

            if (indices.contains(diff)) {
                return {indices[diff], i};
            }

            indices[nums[i]] = i;
        }

        return {};
    }
};
