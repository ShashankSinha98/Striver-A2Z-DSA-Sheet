package bs_on_1d_arrays;
public class ImplementLowerBound {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}
	
	public static int lowerBound(int []arr, int n, int x) {
		
		int left = 0, right = n-1;
		int ans = n;
		
		while(left <= right) {
			int mid = left + (right-left)/2;
			
			if (arr[mid] >= x) {
				ans = mid;
				right = mid-1;
			} else {
				left = mid+1;
			}
		}
		
		return ans;
    }

}
