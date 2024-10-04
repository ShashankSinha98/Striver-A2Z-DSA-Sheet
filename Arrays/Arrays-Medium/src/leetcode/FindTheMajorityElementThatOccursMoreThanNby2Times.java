package leetcode;

public class FindTheMajorityElementThatOccursMoreThanNby2Times {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] nums = new int[] {1,1,2,2,2,1,1};
		System.out.println(new FindTheMajorityElementThatOccursMoreThanNby2Times()
				.majorityElement(nums));
		
	}
	
	public int majorityElement(int[] nums) {
		
		int n = nums.length;
		if(n==1) return nums[0];
		
		int element = nums[0];
		int count = 1;
		
		for(int i=1; i<n; i++) {
			if(nums[i] == element) count++;
			else {
				if(count > 0) count--;
				else {
					element = nums[i];
					count = 1;
				}
			}
		}
		
		return element;  
    }

}
