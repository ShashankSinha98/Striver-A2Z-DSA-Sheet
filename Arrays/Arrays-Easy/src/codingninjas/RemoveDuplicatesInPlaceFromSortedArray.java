package codingninjas;
import java.util.*;

// https://www.codingninjas.com/studio/problems/remove-duplicates-from-sorted-array_1102307?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
public class RemoveDuplicatesInPlaceFromSortedArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = new int[] {1,1,1,2,2,2,3,3};
		ArrayList<Integer> list = new ArrayList<>();
		for(int ai: arr) list.add(ai);
		int ans = removeDuplicates(list, list.size());
		System.out.println(list);
		System.out.println(ans);
	}
	
	public static int removeDuplicates(ArrayList<Integer> arr,int n) {
		if(arr.size() < 2) {
			return arr.size();
		}
		
		int unique_index = 0;
		for(int i=1; i<arr.size(); i++) {
			int ai = arr.get(i);
			if(ai != arr.get(unique_index)) {
				arr.set(++unique_index, ai);
			}
		}
		
		return unique_index+1;
	}

}
