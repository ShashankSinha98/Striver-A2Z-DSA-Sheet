package codingninjas;

import java.util.Arrays;

public class RearrangeArrayElementsBySign {

	public static void main(String[] args) {
		
		int[] a = new int[] {1, 2, -3, -1, -2, 3};
		System.out.println(Arrays.toString(alternateNumbers(a)));
	}
	
	public static int[] alternateNumbers(int[] a) {
		
		int posIdx=0, negIdx=1;
		int[] res = new int[a.length];
		
		for(int i=0; i<a.length; i++) {
			if(a[i] > 0) {
				res[posIdx] = a[i];
				posIdx += 2;
			} else {
				res[negIdx] = a[i];
				negIdx += 2;
			}
		}
		
		return res;
    }

}
