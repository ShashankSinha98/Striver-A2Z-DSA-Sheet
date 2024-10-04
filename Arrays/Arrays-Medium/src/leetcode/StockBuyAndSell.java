package leetcode;

import java.util.Arrays;

public class StockBuyAndSell {

	public static void main(String[] args) {
		int[] prices = new int[] {7,6,4,3,2,1};
		System.out.println(new StockBuyAndSell().maxProfit(prices));
		
	}
	
	public int maxProfit(int[] prices) {
		
		int minPrice = prices[0], maxProfit = 0;
		
		for(int i=1; i<prices.length; i++) {
			maxProfit = Math.max(maxProfit, prices[i]-minPrice);
			minPrice = Math.min(minPrice, prices[i]);
		}
		
		return maxProfit;
    }

}
