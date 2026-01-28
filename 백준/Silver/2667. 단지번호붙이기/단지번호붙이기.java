import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int [][] arr;
    static int cnt;

    static int[] di = {0, 1, 0, -1};
    static int[] dj = {1, 0, -1, 0};

    public static int bfs(int i, int j) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{i, j});
        arr[i][j] = 0;
        cnt = 1;
        while (!q.isEmpty()) {
            int[] cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int ni = cur[0] + di[d];
                int nj = cur[1] + dj[d];
                if (0 <= ni && ni < N && 0 <= nj && nj < N && arr[ni][nj] == 1) {
                    arr[ni][nj] = 0;
                    cnt++;
                    q.add(new int[]{ni, nj});
                }
            }
        }
        return cnt;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < N; j++) {
                arr[i][j] = s.charAt(j) - '0';
            }
        }
        ArrayList<Integer> ans = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == 1) {
                    ans.add(bfs(i, j));
                }
            }
        }
        Collections.sort(ans);
        System.out.println(ans.size());
        for (int x : ans) {
            System.out.println(x);
        }
    }
}
