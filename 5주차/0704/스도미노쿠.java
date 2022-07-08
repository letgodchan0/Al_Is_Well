import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int[][] arr;
    static boolean sudominoku;
    static boolean[][] visited;
    static StringBuilder sb = new StringBuilder();

    public static boolean sudoku(int dpth, int idx, int value) {
        for (int i = 0; i < 9; i++) {
            if (arr[dpth][i] == value) {
                return false;
            }
            if (arr[i][idx] == value) {
                return false;
            }
        }
        int row = (dpth / 3) * 3;
        int col = (idx / 3) * 3;
        for (int i = row; i < row + 3; i++) {
            for (int j = col; j < col + 3; j++) {
                if (arr[i][j] == value) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void dfs(int dpth, int idx) {
        if (sudominoku) return;
        if (idx == 9) {
            dfs(dpth + 1, 0);
            return;
        }
        if (dpth == 9) {
            sudominoku = true;
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    sb.append(arr[i][j]);
                }
                sb.append('\n');
            }
            return;
        }
        int[] dx = { 0, 1 };
        int[] dy = { 1, 0 };
        if (arr[dpth][idx] == 0) {
            for (int i = 1; i <= 9; i++) {
                if (sudoku(dpth, idx, i)) {
                    arr[dpth][idx] = i;
                    for (int k = 0; k < 2; k++) {
                        int nx = idx + dy[k];
                        int ny = dpth + dx[k];
                        if (ny < 9 && nx < 9 && arr[ny][nx] == 0) {
                            for (int j = 1; j <= 9; j++) {
                                if (i != j && !visited[i][j] && sudoku(ny, nx, j)) {
                                    arr[ny][nx] = j;
                                    visited[i][j] = visited[j][i] = true;
                                    dfs(dpth, idx + 1);
                                    arr[ny][nx] = 0;
                                    visited[i][j] = visited[j][i] = false;
                                }
                            }
                        }
                    }
                    arr[dpth][idx] = 0;
                }
            }
            return;
        }
        dfs(dpth, idx + 1);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cnt = 1;
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) break;
            arr = new int[9][9];
            visited = new boolean[10][10];
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine(), " ");
                int u = Integer.parseInt(st.nextToken());
                String lu = st.nextToken();
                int v = Integer.parseInt(st.nextToken());
                String lv = st.nextToken();
                visited[u][v] = visited[v][u] = true;
                arr[lu.charAt(0) - 'A'][lu.charAt(1) - '1'] = u;
                arr[lv.charAt(0) - 'A'][lv.charAt(1) - '1'] = v;
            }
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int i = 1; i <= 9; i++) {
                String str = st.nextToken();
                arr[str.charAt(0) - 'A'][str.charAt(1) - '1'] = i;
            }
            sudominoku = false;
            sb.append("Puzzle ").append(cnt++).append("\n");
            dfs(0, 0);
        }
        System.out.print(sb);
    }
}