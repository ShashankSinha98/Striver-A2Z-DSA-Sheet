import java.util.*;

public class SortCharactersByFrequency {

	public static void main(String[] args) {
		String s = "Aabb";
		String res = new SortCharactersByFrequency().frequencySort(s);
		System.out.println(res);
	}
	
    public String frequencySort(String s) {
    	int n = s.length();
    	Map<Character, Integer> cmap = new HashMap<>();
    	
    	for(Character c: s.toCharArray()) {
    		cmap.put(c, cmap.getOrDefault(c, 0) + 1);
    	}
    	
    	List<Character> clist[] = new List[n+1];
    	
    	for(Character c: cmap.keySet()) {
    		int freq = cmap.get(c);
    		List<Character> li = clist[freq];
    		
    		if(li==null) {
    			li = new ArrayList<>();
    			clist[freq] = li;
    		}
    		
    		li.add(c);
    	}
    	
    	
    	StringBuilder res = new StringBuilder();
    	for(int i=n; i>=0; i--) {
    		if(clist[i] != null) {
    			List<Character> li = clist[i];
    			
    			for(Character c: li) {
    				int tmp = i;
    				while(tmp != 0) {
    					res.append(c);
    					tmp--;
    				}
    			}
    		}
    	}
    	
    	return res.toString();
    }

}
