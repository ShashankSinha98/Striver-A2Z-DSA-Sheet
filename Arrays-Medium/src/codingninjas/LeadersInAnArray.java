package codingninjas;

import java.util.ArrayList;
import java.util.List;

public class LeadersInAnArray {

	public static void main(String[] args) {
		
		int[] a = new int[] {10, 22, 12, 3, 0, 6};
		System.out.println(superiorElements(a));

	}
	
	public static List<Integer> superiorElements(int[] a) {
        int n = a.length;
		int maxElement = a[n-1];
		List<Integer> res = new ArrayList<>();
		res.add(maxElement);
		
		for(int i=n-2; i>=0; i--) {
			if(a[i] > maxElement) {
				maxElement = a[i];
				res.add(a[i]);
			}
		}
		reverse(res, 0, res.size()-1);
		return res;
    }
	
	private static void reverse(List<Integer> nums, int start, int end) {
		while(start < end) {
			int temp = nums.get(start);
			nums.set(start, nums.get(end));
			nums.set(end, temp);
			start++; end--;
		}
	}

}
