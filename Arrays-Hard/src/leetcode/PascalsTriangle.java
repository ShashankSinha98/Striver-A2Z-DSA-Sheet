package leetcode;
import java.util.*;
public class PascalsTriangle {

	public static void main(String[] args) {
		
		int numRows = 1;
		List<List<Integer>> res = new PascalsTriangle().generate(numRows);
		for(List<Integer> r: res) {
			System.out.println(r);
		}
	}
	
	public List<List<Integer>> generate(int numRows) {
		List<List<Integer>> res = new ArrayList<>();
		
		for(int r=1; r<=numRows; r++) {
			int[] a = new int[r];
			a[0] = a[a.length-1] = 1;
			
			if(res.size()<2) {
				res.add(toList(a));
				continue;
			}
			
			for(int i=1; i<r-1; i++) {
				List<Integer> pArr = res.get(res.size()-1);
				a[i] = pArr.get(i-1) + pArr.get(i);
			}
			
			res.add(toList(a));
		}
		
		return res;
    }
	
	private List<Integer> toList(int[] a) {
		List<Integer> res = new ArrayList<>();
		for(int ai: a) {
			res.add(ai);
		}
		
		return res;
	}

}
