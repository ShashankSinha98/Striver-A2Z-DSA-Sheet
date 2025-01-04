public class GeekTraining {
    public static void main(String[] args) {
        
    }

    public int maximumPoints(int arr[][], int N) {
        int[][] dp = new int[N][3];
        dp[0][0] = Math.max(arr[0][1], arr[0][2]);
        dp[0][1] = Math.max(arr[0][0], arr[0][2]);
        dp[0][2] = Math.max(arr[0][0], arr[0][1]);

        for(int di=1; di<N; di++) {
            for(int k=0; k<=2; k++) {
                if(k==0) {
                    dp[di][0] = Math.max(arr[di][1]+dp[di-1][1], arr[di][2]+dp[di-1][2]);
                } else if(k==1) {
                    dp[di][1] = Math.max(arr[di][0]+dp[di-1][0], arr[di][2]+dp[di-1][2]);
                } else if(k==2) {
                    dp[di][2] = Math.max(arr[di][0]+dp[di-1][0], arr[di][1]+dp[di-1][1]);
                }
            }
        }
        return Math.max(dp[N-1][0],Math.max(dp[N-1][1],dp[N-1][2]));
    }
}
