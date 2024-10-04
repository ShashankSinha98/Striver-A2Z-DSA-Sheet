package codingninjas;

public class LongestSubarrayWithGivenSumKPositives {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int[] a = new int[] {5,4,1,1,1};
		int k = 3;
		System.out.println(longestSubarrayWithSumK(a, k));

	}

	public static int longestSubarrayWithSumK(int []a, long k) {
		int l = 0, r = 0;
		long currSum = 0;
		int longestSubArrLen = 0;
		int n = a.length;
		
		while(r < n) {
			
			currSum += a[r];
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
			
			r++;
		}
		return longestSubArrLen;
    }

}
