package leetcode;

import java.util.*;

public class LongestConsecutiveSequence {

	public static void main(String[] args) {
		
		int[] nums = new int[] {0,3,7,2,5,8,4,6,0,1};
		System.out.println(new LongestConsecutiveSequence().longestConsecutive(nums));
	}
	
	public int longestConsecutive(int[] nums) {
		
		if(nums.length==0) return 0;
		
        Set<Integer> set = new HashSet<>();
        for(int i: nums) { set.add(i); }
        
        int longest = 1;
        for(int i=0; i<nums.length; i++) {
        	if(!set.contains(nums[i]-1)) {
        		int curr = 1, target = nums[i] + 1;
        		while(set.contains(target)) {
        			curr += 1;
        			longest = Math.max(longest, curr);
        			target += 1;
        		}
        	}
        }
        
        return longest;
    }

}
