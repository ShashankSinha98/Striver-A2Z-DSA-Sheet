package leetcode;

public class CountMaximumConsecutiveOnesInTheArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = new int[] {1,0,1,1,0,1};
		System.out.println(new CountMaximumConsecutiveOnesInTheArray().findMaxConsecutiveOnes(nums));
	}
	
	public int findMaxConsecutiveOnes(int[] nums) {
        int maxConsecutiveOnes = 0, currConsecutiveOnes = 0;
        
        for(int i: nums) {
        	if(i==1) {
        		maxConsecutiveOnes = Integer.max(maxConsecutiveOnes, ++currConsecutiveOnes);
        	} else {
        		currConsecutiveOnes = 0;
        	}
        }
        
        return maxConsecutiveOnes;
    }

}
