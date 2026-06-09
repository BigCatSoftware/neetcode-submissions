class Solution {
    public int[] twoSum(int[] nums, int target) {
        var indices = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];

            if (indices.containsKey(diff)) {
                return new int[]{indices.get(diff), i};
            }

            indices.put(nums[i], i);
        } 

        return new int[2];
    }
}
