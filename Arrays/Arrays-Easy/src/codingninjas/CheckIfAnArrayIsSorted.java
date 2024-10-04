package codingninjas;
// https://www.codingninjas.com/studio/problems/ninja-and-the-sorted-check_6581957?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf
public class CheckIfAnArrayIsSorted {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] arr = new int[] {1,2,3,4,5};
		System.out.println(isSorted(arr.length, arr));
	}
	
	public static int isSorted(int n, int []a) {
        if(a.length < 2) return 1;
        
		for(int i=1; i<a.length; i++) {
			if(a[i-1] > a[i]) 
				return 0;
		}
		
		return 1;
    }

}
