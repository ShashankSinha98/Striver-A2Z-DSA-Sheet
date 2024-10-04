package leetcode;

import java.util.Arrays;

public class SortAnArrayOf0s1sAnd2s {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums = new int[] {2,0,1};
		new SortAnArrayOf0s1sAnd2s().sortColors(nums);
		System.out.println(Arrays.toString(nums));
	}
	
	public void sortColors(int[] nums) {
		int n = nums.length;
		int low = 0, mid = 0, high = n-1;
		
		while(mid <= high) {
			if(nums[mid] == 0) {
				swap(nums, mid, low);
				low++; mid++;
			} else if(nums[mid] == 1) {
				mid++;
			} else { // 2
				swap(nums, mid, high);
				high--;
			}
		}
    }
	
	private static void swap(int[] arr, int i, int j) {
		int temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

}
