package codingninjas;

import java.util.*;

public class CountSubarraySumEqualsK {

	public static void main(String[] args) {
		int[] nums = new int[] {1,2,3,-3,1,1,1,4,2,-3};
		int k = 3;
		System.out.println(new CountSubarraySumEqualsK().subarraySum(nums, k));
	}
	
	public int subarraySum(int[] nums, int k) {
		Map<Long, Integer> map = new HashMap<>();
		long cs = 0;
		int cnt = 0;
		
		for(int i=0; i<nums.length; i++) {
			cs += nums[i];
			
			if(cs==k) cnt++;
			long remm = cs - k;
			
			if(map.containsKey(remm)) {
				cnt += map.get(remm);
			}
			
			if(map.containsKey(cs)) {
				int val = map.get(cs);
				map.put(cs, val+1);
			} else {
				map.put(cs, 1);
			}
		}
		
		return cnt;
    }

}
