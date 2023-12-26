package leetcode;

import java.util.*;

public class TwoSum {
	
	public static void main(String... args) {
		int[] nums = new int[] {3,3};
		int target = 6;
		System.out.println(Arrays.toString(twoSum(nums, target)));
	}

	public static int[] twoSum(int[] nums, int target) {
		
		Map<Integer, Integer> map = new HashMap<>();
		
		for(int i=0; i<nums.length; i++) {
			int n = nums[i];
			int remm = target - n;
			
			if(map.containsKey(remm)) {
				return new int[] {map.get(remm), i};
			} else {
				map.put(n, i);
			}
		}
	
		
		return new int[] {-1, -1};
    }
}
