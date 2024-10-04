package codingninjas;
import java.util.ArrayList;

// https://www.codingninjas.com/studio/problems/rotate-array_1230543?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
// Rotate to Left
public class RotateArrayByKElements {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = new int[] {1,2,3,4,5,6,7};
		ArrayList<Integer> list = new ArrayList<>();
		for(int ai: arr) list.add(ai);
		
		System.out.println(rotateArray(list, 3));
	}
	
	public static ArrayList<Integer> rotateArray(ArrayList<Integer> arr, int k) {
        // Write your code here.
		
		// rotate [0:k-1] elements
		arr = rotate(arr, 0, k-1);
		
		// rotate [k:n-1] elements
		arr = rotate(arr, k, arr.size()-1);
		
		// rotate [0,n-1] elements
		arr = rotate(arr, 0, arr.size()-1);
		
		return arr;
    }
	
	private static ArrayList<Integer> rotate(ArrayList<Integer> arr, int left, int right) {
		while(left < right) {
			int temp = arr.get(left);
			arr.set(left, arr.get(right));
			arr.set(right, temp);
			left++; right--;
		}
		return arr;
	}

}
