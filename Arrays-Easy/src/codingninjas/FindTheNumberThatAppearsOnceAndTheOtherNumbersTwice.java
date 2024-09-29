package codingninjas;

public class FindTheNumberThatAppearsOnceAndTheOtherNumbersTwice {

	public static void main(String[] args) {
		
		int[] arr = new int[] {1,1,2,3,3};
		System.out.println(getSingleElement(arr));
	}
	
	public static int getSingleElement(int[] arr){
        int res = 0;
        
        for(int i: arr) {
        	res ^= i;
        }
        
        return res;
    }

}
