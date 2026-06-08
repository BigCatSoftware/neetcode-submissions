class Solution {
    public boolean hasDuplicate(int[] nums) {
        var numSet = new HashSet<Integer>();

        for (int num : nums) {
            if (numSet.contains(num)) {
                return true;
            }
            numSet.add(num);
        }

        return false;
    }
}