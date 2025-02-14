package codingninjas;

import java.util.*;
//https://www.codingninjas.com/studio/problems/sorted-array_6613259?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse&leftPanelTabValue=SUBMISSION
public class UnionOfTwoSortedArrays {

	public static void main(String[] args) {
		
		int[] a = new int[]{1,2,3,4,5,6,7,8,9,10};
		int[] b = new int[]{2,3,4,4,5,11,12};
		
		System.out.println(sortedArray(a, b));
	}
	
	public static List<Integer> sortedArray(int []a, int []b) {
		int i=0, j=0;
		List<Integer> res = new ArrayList<>();
		
		while(i<a.length && j<b.length) {
			if(a[i] < b[j]) {
				if(res.isEmpty() || res.get(res.size()-1)!=a[i]) {
					res.add(a[i]);
				}
				i++;
			} else if(b[j] < a[i]) {
				if(res.isEmpty() || res.get(res.size()-1)!=b[j]) {
					res.add(b[j]);
				}
				j++;
			} else {
				if(res.isEmpty() || res.get(res.size()-1)!=b[j]) {
					res.add(b[j]);
				}
				i++; j++;
			}
		}
		
		if(i < a.length) {
			res.addAll(removeDuplicates(a, a.length, i));
		} else if(j < b.length) {
			res.addAll(removeDuplicates(b, b.length, j));
		}
		
		return res;
    }
	
	public static List<Integer> removeDuplicates(int[] arr,int n, int startIdx) {
		if(n==0 || startIdx >= n) return new ArrayList<>();
		
		int unique_index = startIdx;
		for(int i=startIdx+1; i<n; i++) {
			int ai = arr[i];
			if(ai != arr[unique_index]) {
				arr[++unique_index] = ai;
			}
		}
		
		List<Integer> res = new ArrayList<>();
		for(int i=startIdx; i<=unique_index; i++) {
			res.add(arr[i]);
		}
		
		return res;
	}

}
