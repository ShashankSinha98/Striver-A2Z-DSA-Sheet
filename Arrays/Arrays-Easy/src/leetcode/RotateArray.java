package leetcode;

// https://leetcode.com/problems/rotate-array/description/
public class RotateArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	 public void rotate(int[] arr, int k) {
	        int n = arr.length;
	        if (n==1) return;
	        k = k % n;
			// rotate [0:n-k-1] elements
			arr = rotate(arr, 0, n-k-1);
			
			// rotate [n-k:n-1] elements
			arr = rotate(arr, n-k, n-1);
			
			// rotate [0,n-1] elements
			arr = rotate(arr, 0, n-1);		
		 }
		 
		 private static int[] rotate(int[] arr, int left, int right) {
			while(left < right) {
				int temp = arr[left];
				arr[left] = arr[right];
				arr[right] = temp;
				left++; right--;
			}
			return arr;
		}

}
