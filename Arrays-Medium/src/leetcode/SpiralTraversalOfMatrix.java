package leetcode;
import java.util.*;

public class SpiralTraversalOfMatrix {

	public static void main(String[] args) {

		int[][] matrix = new int[][] {{1,2,3,4},
									  {5,6,7,8},
									  {9,10,11,12}};
									  
		System.out.println(new SpiralTraversalOfMatrix().spiralOrder(matrix));
	}
	
	public List<Integer> spiralOrder(int[][] matrix) {
		int nr = matrix.length, nc= matrix[0].length;
		
		
		List<Integer> res = new ArrayList<>();
		int top=0, bottom=nr-1, left=0, right=nc-1;
		while(left<=right || top<=bottom) {
			// left to right
			for(int i=left; i<=right; i++) {
				res.add(matrix[top][i]);
			}
			
			top++;
			
			// top to bottom
			for(int i=top; i<=bottom; i++) {
				res.add(matrix[i][right]);
			}
			
			right--;
			
			if(top<=bottom) { // we still have row to print
				// right to left
				for(int i=right; i>=left; i--) {
					res.add(matrix[bottom][i]);
				}
			}
			
			bottom--;
			
			if(left<=right) { // we still haev column to print
				// bottom to top
				for(int i=bottom; i>=top; i--) {
					res.add(matrix[i][left]);
				}
			}
			
			left++;
		}
		
		return res;
    }

}
