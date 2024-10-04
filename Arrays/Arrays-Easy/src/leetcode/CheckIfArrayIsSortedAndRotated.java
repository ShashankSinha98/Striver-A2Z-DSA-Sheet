package leetcode;

public class CheckIfArrayIsSortedAndRotated {

	public static void main(String[] args) {
		int[] nums = new int[] {2,4,1,3};
		System.out.println(new CheckIfArrayIsSortedAndRotated().check(nums));
	}
	
	public boolean check(int[] nums) {
		int n = nums.length;
		
		if(n<=1) return true;
		
		int dips = 0;
		
		for(int i=0; i<n; i++) {
			// check if there is a dip, take modulo of index to avoid out of bound 
			if(nums[i] > nums[(i+1) % n]) 
				dips++;
			
			// If there are more than 2 dips, then it's not sorted and rotated
			if(dips > 1) return false;
		}
		
		return true;
    }

}
