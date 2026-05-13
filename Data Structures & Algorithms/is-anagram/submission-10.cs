public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) {
            return false;
        }

        int[] counter = new int[26];
        foreach (char c in s) {
            counter[c - 'a']++;
        }

        foreach (char c in t) {
            counter[c - 'a']--;
        }

        foreach (int num in counter) {
            if (num != 0) {
                return false;
            }
        }

        return true;
    }
}
