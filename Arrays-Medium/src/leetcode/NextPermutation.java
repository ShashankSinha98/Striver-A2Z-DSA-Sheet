package leetcode;

import java.util.Arrays;

public class NextPermutation {

	public static void main(String[] args) {
		
		int[] arr = new int[] {2,1,5,4,3,0,0};
		new NextPermutation().nextPermutation(arr);
		System.out.println(Arrays.toString(arr));

	}
	
	public void nextPermutation(int[] nums) {
		int n = nums.length;
		int idx = -1;
		for(int i=n-2; i>=0; i--) {
			if(nums[i] < nums[i+1]) {
				idx = i;
				break;
			}
		}
		
		if(idx==-1) {
			reverse(nums, 0, n-1);
			return;
		}
		
		for(int i=n-1; i>idx; i--) {
			if(nums[i] > nums[idx]) {
				swap(nums, i, idx);
				reverse(nums, idx+1, n-1);
				return;
			}
		}
    }
	
	private void reverse(int[] nums, int start, int end) {
		while(start < end) {
			swap(nums, start, end);
			start++; end--;
		}
	}
	
	private void swap(int[] arr, int i, int j) {
		int temp =  arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

}
