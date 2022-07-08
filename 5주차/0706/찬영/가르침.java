import java.util.Scanner;

public class Main {
    static int N, K, ans;
    static boolean[][] word;
    static boolean[] visit;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt(); 
        K = sc.nextInt(); 

        word = new boolean[N][26];
        for (int i = 0; i < N; i++) {
            String tmp = sc.next();
            for (int j = 0; j < tmp.length(); j++) {
                word[i][tmp.charAt(j) - 'a'] = true;
            }
        }
        visit = new boolean[26];
        ans = 0;
        solve(0, 0);
        System.out.println(ans);
    }

    private static void solve(int index, int depth) {
        if (depth == K) {
            check();
            return;
        }
        for (int i = index; i < 26; i++) {
            if (!visit[i]) {
                visit[i] = true;
                solve(i, depth + 1);
                visit[i] = false;
            }
        }

    }

    private static void check() {
        int ret = 0;

        boolean flag = true;
        for (int k = 0; k < N; k++) {
            flag = true;
            for (int i = 0; i < 26; i++) {
                if (word[k][i] && !visit[i]) {
                    flag = false;
                    break;
                }
            }
            if (flag)
                ret++;
        }

        ans = Math.max(ret, ans);
    }
}