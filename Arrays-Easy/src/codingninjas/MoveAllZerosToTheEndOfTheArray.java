package codingninjas;

import java.util.Arrays;

public class MoveAllZerosToTheEndOfTheArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = new int[] {1,0,2,3,0,4,0,1};
		System.out.println(Arrays.toString(moveZeros(arr.length, arr)));
	}
	
	public static int[] moveZeros(int n, int []a) {
        int z = -1;
        for(int i=0; i<n; i++) {
        	if(a[i]!=0) {
        		if(z!=-1) {
	        		int temp = a[z];
	        		a[z] = a[i];
	        		a[i] = temp;
	        		z++;
        		}
        	} else {
        		if(z==-1) 
        			z = i;
        	}
        }
        return a;
    }

}
