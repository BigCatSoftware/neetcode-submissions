class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.size() != t.size()) {
            return false;
        }

        std::unordered_map<int, int> indices{};
        for (char c : s) {
            int index = static_cast<int>(c - 'a');
            indices[index]++; 
        }

        for (char c : t) {
            int index = static_cast<int>(c - 'a');
            indices[index]--;
        }

        for (const std::pair<const int, int>& p : indices) {
            if (p.second != 0) {
                return false;
            }
        }

        return true;
    }
};
