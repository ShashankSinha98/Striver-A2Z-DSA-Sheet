package bs_on_1d_arrays;

import java.util.Arrays;

public class FloorAndCeilInSortedArray {

	public static void main(String[] args) {

		int[] a = new int[] {3, 4, 4, 7, 8, 10};
		int x = 7;
		System.out.println(Arrays.toString(getFloorAndCeil(a, a.length, x)));
	}
	
    public static int[] getFloorAndCeil(int[] a, int n, int x) {
    		int left = 0, right = n-1;
    		int floor = -1;
    		// find floor
    		while(left <= right) {
    			int mid = left + (right - left) / 2;
    			if(a[mid] == x) {
    				return new int[] {x,x};
    			} else if(a[mid] < x) {
    				floor = a[mid];
    				left = mid+1;
    			} else {
    				right = mid-1;
    			}
    		}
    		
    		int ceil = -1;
    		left = 0; right = n-1;
    		// find ceil
    		while(left <= right) {
    			int mid = left + (right - left) / 2;
    			
    			if(a[mid] < x) {
    				left = mid+1;
    			} else {
    				ceil = a[mid];
    				right = mid-1;
    			}
    		}
    		
    		return new int[] {floor, ceil};
      }

}
