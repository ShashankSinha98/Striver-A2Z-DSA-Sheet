import java.util.Arrays;

// https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960?utm_source=striver&utm_medium=website&utm_campaign=codestudio_a_zcourse&leftPanelTabValue=PROBLEM&count=25&search=&sort_entity=order&sort_order=ASC
public class FindSecondSmallestAndSecondLargestElementInAnArray {

	public static void main(String[] args) {
		int[] arr = new int[]{1,2,3,4,5};
		System.out.println(Arrays.toString(getSecondOrderElements(arr.length, arr)));
	}
	
	public static int[] getSecondOrderElements(int n, int []a) {
		if(a.length < 2) {
			return new int[]{-1, -1};
		}
		
		int small = Integer.MAX_VALUE, second_small = Integer.MAX_VALUE;
		int large = Integer.MIN_VALUE, second_large = Integer.MIN_VALUE;
		for(int ai: a) {
			if(ai != small) {
				if(ai < small) {
					second_small = small;
					small = ai;
				} else if(ai < second_small) 
					second_small = ai;
			}
			
			if(ai != large) {
				if(ai > large) {
					second_large = large;
					large = ai;
				} else if(ai > second_large) {
					second_large = ai;
				}
			}
		}
		
		if(second_small==Integer.MAX_VALUE) 
			second_small = -1;
		if(second_large==Integer.MIN_VALUE)
			second_large = -1;
		
		return new int[] {second_large, second_small};
    }

}
