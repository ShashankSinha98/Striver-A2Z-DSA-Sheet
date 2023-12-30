package leetcode;

import java.util.Arrays;

public class SetMatrixZero {

	public static void main(String[] args) {
		int[][] matrix = new int[][] { { 1, 1, 1, 1 }, { 1, 0, 1, 1 }, { 1, 1, 0, 1 }, { 0, 1, 1, 1 } };
		int[][] matrix2 = new int[][] {{0,1,2,0},{3,4,5,2},{1,3,1,5}};
		int[][] matrix3 = new int[][] {{1,1,1},{1,0,1},{1,1,1}};
		int[][] matrix4 = new int[][] {{1,0,3}};
		new SetMatrixZero().setZeroes(matrix4);

		
		for(int[] ai: matrix4) {
			System.out.println(Arrays.toString(ai));
		}
		
	}

	public void setZeroes(int[][] matrix) {

		int n = matrix.length;
		int m = matrix[0].length;
		boolean rowContainsZero = false, colContainsZero = false;
		
		for (int r = 0; r < n; r++) {
			for (int c = 0; c < m; c++) {
				if (matrix[r][c] == 0) {
					
					if(c==0) rowContainsZero = true;
					if(r==0) colContainsZero = true;
					
					matrix[r][0] = 0;					
					matrix[0][c] = 0;
				}
			}
		}		
	
		// Iterate and set 0 for inner matrix
		for (int r = 1; r < n; r++) {
			for (int c = 1; c < m; c++) {
				if (matrix[r][0] == 0 || matrix[0][c] == 0 ) {
					matrix[r][c] = 0;
				}
			}
		}
		
		if(rowContainsZero) {
			for (int r = 0; r < n; r++)
				matrix[r][0] = 0;
		} 
		
		if(colContainsZero) {
			for (int c = 0; c < m; c++)
				matrix[0][c] = 0;
		} 
	}

}
