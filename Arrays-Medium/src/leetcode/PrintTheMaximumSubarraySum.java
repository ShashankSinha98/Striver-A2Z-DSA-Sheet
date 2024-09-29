package leetcode;

import java.util.Arrays;

public class PrintTheMaximumSubarraySum {

	public static void main(String[] args) {
		int[] nums = new int[] {-2, -5, 6, -2, -3, 1, 5, -6};
		System.out.println(Arrays.toString(subarrayWithMaxSum(nums)));
	}
	
	private static int[] subarrayWithMaxSum(int[] nums) {
		int n = nums.length;
		
		if(n==1) return nums;
		
		int localStartIdx = 0, finalStartIdx = -1, finalEndIdx = -1;
		int currSum = 0, maxSum = Integer.MIN_VALUE;
		for(int i=0; i<n; i++) {
			if(currSum == 0) {
				localStartIdx = i;
			}
			
			currSum += nums[i];
			
			if(currSum > maxSum) {
				maxSum = currSum;
				finalStartIdx = localStartIdx;
				finalEndIdx = i;
			}
			
			if(currSum < 0) {
				currSum = 0;
			}
		}
		System.out.println("finalStartIdx: "+finalStartIdx+", finalEndIdx: "+finalEndIdx);
		if(finalStartIdx != -1 && finalEndIdx != -1) {
			int[] res = new int[finalEndIdx-finalStartIdx+1];
			for(int i=finalStartIdx; i<=finalEndIdx; i++) {
				res[i-finalStartIdx] = nums[i]; 
			}
			
			return res;
		}
		
		return null;
	}

}
