package leetcode;

public class MaximumSubarraySumInAnArray {

	public static void main(String[] args) {
		int[] nums = new int[] {-2,1,-3,4,-1,2,1,-5,4};
		System.out.println(new MaximumSubarraySumInAnArray().maxSubArray(nums));

	}
	
	public int maxSubArray(int[] nums) {
        int currSum = 0;
        int maxSum = Integer.MIN_VALUE;
        
        for(int i=0; i<nums.length; i++) {
        	currSum += nums[i];
        	
        	maxSum = Math.max(maxSum, currSum);
        	
        	if(currSum < 0) {
        		currSum = 0;
        	}
        }
        
        return maxSum;
    }

}
