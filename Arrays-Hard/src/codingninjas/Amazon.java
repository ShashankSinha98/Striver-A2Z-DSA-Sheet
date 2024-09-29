package codingninjas;

import java.util.*;

public class Amazon {

	public static void main(String[] args) {
		
		List<String> orders = new ArrayList<>();
//		orders.add("zid 93 12");
//		orders.add("fp kindle book");
//		orders.add("10a echo show");
//		orders.add("17g 12 25 6");
//		orders.add("ab1 kindle book");
//		orders.add("125 echo dot second generation");

		orders.add("t2 13 121 98");
		orders.add("r1 box ape bit");
		orders.add("b4 xi me nu");
		orders.add("br8 eat nim did");
		orders.add("w1 has uni gry");
		orders.add("f3 52 54 31");
		
		System.out.println(sortPrime(orders));

	}
	
	public static List<String> sortPrime(List<String> orders) {
		
		List<String> primeOrders = new ArrayList<>();
		List<String> nonPrimeOrders = new ArrayList<>();
		
		for(String order: orders) {
			String ordername = getOrderName(order);
			char fchar = ordername.charAt(0);
			if(fchar >= 'a' && fchar <= 'z') {
				primeOrders.add(order);
			} else {
				nonPrimeOrders.add(order);
			}
		}
		
		Collections.sort(primeOrders, new PrimeSort());
		
		primeOrders.addAll(nonPrimeOrders);
		
		return primeOrders;
	}

	private static String getOrderName(String order) {
		int i=0;
		while(i < order.length() && order.charAt(i) != ' ') {
			i++;
		}
		
		return order.substring(i+1);
	}
	
	private static String getOrderID(String order) {
		int i=0;
		while(i < order.length() && order.charAt(i) != ' ') {
			i++;
		}
		
		return order.substring(0, i);
	}
	
	static class PrimeSort implements Comparator<String> {

		@Override
		public int compare(String order1, String order2) {
			String orderID1 = getOrderID(order1);
			String orderID2 = getOrderID(order2);
			String orderName1 = getOrderName(order1);
			String orderName2 = getOrderName(order2);
			
			int compareName = orderName1.compareTo(orderName2);
			if(compareName < 0) { // order 1 is smaller
				return -1;
			} else if(compareName > 0) { // order2 is smaller
				return 1;
			} else {
				return orderID1.compareTo(orderID2);
			}
		}
		
	}
}
