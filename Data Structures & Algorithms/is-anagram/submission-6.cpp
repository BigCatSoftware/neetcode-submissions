class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        std::array<int, 26> counter{};

        for (char c : s) {
            size_t index = static_cast<int>(c - 'a');
            counter[index]++;
        }

        for (char c : t) {
            size_t index = static_cast<int>(c - 'a');
            counter[index]--;
        }

        for (int num : counter) {
            if (num != 0) {
                return false;
            }
        }

        return true;
    }
};
