package codingninjas;

public class LongestSubarrayWithGivenSumKPositives {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[] a = new int[] {2,3,5};
		int k = 2;
		System.out.println(longestSubarrayWithSumK(a, k));

	}
	
	public static int longestSubarrayWithSumK(int []a, long k) {
		int l = 0, r = 0;
		int currSum = a[0];
		int longestSubArrLen = 0;
		int n = a.length;
		
		while(r < n) {
			// move left pointer to right and decrease window size
			while(currSum > k) {
				if(l <= r) {
					currSum -= a[l];
					l++;
				}
			}
			
			// compute longest subarray length
			if(currSum == k) {
				longestSubArrLen = Math.max(longestSubArrLen, r - l + 1);
			}
			
			// move right, if within arr no bound, add no to curr sum
			r++;
			if(r < n) {
				currSum += a[r];
			}
		}
		return longestSubArrLen;
    }

}
