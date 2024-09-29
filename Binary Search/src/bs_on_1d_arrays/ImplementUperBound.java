package bs_on_1d_arrays;

public class ImplementUperBound {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = new int[] {1, 4, 7, 8, 10};
		int x = 7;
		System.out.println(upperBound(arr, x, arr.length));
	}
	
    public static int upperBound(int []arr, int x, int n){
    	int left = 0, right = n-1;
		int ans = n;
		
		while(left <= right) {
			int mid = left + (right-left)/2;
			
			if (arr[mid] > x) {
				ans = mid;
				right = mid-1;
			} else {
				left = mid+1;
			}
		}
		
		return ans;
    }

}
