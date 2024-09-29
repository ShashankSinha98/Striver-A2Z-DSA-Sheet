package leetcode;

import java.util.Arrays;

public class RotateImageBy90Degree {

	public static void main(String[] args) {
		int[][] m = new int[][] {{5,1,9,11},
								 {2,4,8,10},
								 {13,3,6,7},
								 {15,14,12,16}};
								 
      new RotateImageBy90Degree().rotate(m);
      for(int[] ai: m) {
    	  System.out.println(Arrays.toString(ai));
      }
	}
	
	
	public void rotate(int[][] m) {
		
		int n = m.length;
		int l=0, r=n-1, t=0, b=n-1;
		
		while(l<=r && t<=b) {
			for(int i=0; i<r-l; i++) {
				int temp = m[t][l+i];
				m[t][l+i] = m[b-i][l];
				m[b-i][l] = m[b][r-i];
				m[b][r-i] = m[t+i][r];
				m[t+i][r] = temp;
			}
			l++; r--; t++; b--;
		}
    }

}
