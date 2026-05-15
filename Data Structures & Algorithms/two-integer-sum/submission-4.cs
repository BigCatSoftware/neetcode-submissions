public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> indices = new();

        int i = 0;
        foreach (int num in nums) {
            int difference = target - num;
            if (indices.ContainsKey(difference)) {
                return [indices[difference], i];
            }
            indices[num] = i;
            i++;
        }

        return [];
    }
}
