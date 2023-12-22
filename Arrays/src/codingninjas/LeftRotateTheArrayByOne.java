package codingninjas;
import java.util.* ;
import java.io.*; 

// https://www.codingninjas.com/studio/problems/left-rotate-an-array-by-one_5026278?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
public class LeftRotateTheArrayByOne {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = new int[] {1,2,3,4,5};
		System.out.println(Arrays.toString(rotateArray(arr, arr.length)));
	}
	
	static int[] rotateArray(int[] arr, int n) {
		 
		if(n < 2)
			return arr;
		
		int arr_0 = arr[0];
		for(int i=1; i<n; i++) {
			arr[i-1] = arr[i];
		}
		arr[n-1] = arr_0;
		
		return arr;
    }

}
