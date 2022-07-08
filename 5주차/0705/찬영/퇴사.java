import java.util.Scanner;

public class Main {
	
    public static int[][] inputAry;
    public static int answer = Integer.MIN_VALUE;
	
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
		
        inputAry = new int[n+1][2];
		
        for(int i = 0; i < n; i++) {
            inputAry[i][0] = sc.nextInt();
            inputAry[i][1] = sc.nextInt();
        }
		
        dfs(n,0,0);
        System.out.println(answer);
    }
    public static void dfs(int n, int depth, int sum) {
        if(depth == n) {
            answer = Math.max(answer, sum);
            return;
        }
        if(depth + inputAry[depth][0] <= n) {
            dfs(n, depth + inputAry[depth][0], sum + inputAry[depth][1]);
        }
        dfs(n, depth+1, sum);
    }
}