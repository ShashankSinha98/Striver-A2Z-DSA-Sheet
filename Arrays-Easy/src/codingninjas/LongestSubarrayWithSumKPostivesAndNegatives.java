package codingninjas;

import java.util.*;

public class LongestSubarrayWithSumKPostivesAndNegatives {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] nums = new int[] {1,2,1,0,1};
		int k = 4;
		System.out.println(getLongestSubarray(nums, k));

	}
	
	public static int getLongestSubarray(int[] nums, int k) {
		Map<Long, Integer> prefixSumIndexes = new HashMap<>();
		long currSum = 0;
		int longestSubarrLen = 0;
		int n = nums.length;
		
		for(int i=0; i<n; i++) {
			currSum += nums[i];
			
			if(currSum == k) {
				longestSubarrLen = Math.max(longestSubarrLen, i+1);
			}
			
			long remm = currSum - k;
			if(prefixSumIndexes.containsKey(remm)) {
				int subArrLen = i - prefixSumIndexes.get(remm);
				longestSubarrLen = Math.max(longestSubarrLen, subArrLen);
			}
			
			if(!prefixSumIndexes.containsKey(currSum)) {
				prefixSumIndexes.put(currSum, i);
			}
		}
		
		return longestSubarrLen;
	}

}
