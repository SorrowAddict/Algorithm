import java.io.*;
import java.util.*;

public class Main {

    static int N;
    static int[][] arr;
    static boolean[][] active;
    static int[] parent;

    static int[] di = {1, 0, -1, 0};
    static int[] dj = {0, 1, 0, -1};

    static int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    static void union(int a, int b) {
        a = find(a);
        b = find(b);
        if (a != b) parent[b] = a;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        active = new boolean[N][N];

        List<int[]> cells = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
                cells.add(new int[]{arr[i][j], i, j});
            }
        }
        cells.sort((a, b) -> b[0] - a[0]);

        parent = new int[N * N];
        for (int i = 0; i < N * N; i++) parent[i] = i;
        int cnt = 0;
        int ans = 0;
        int idx = 0;
        while (idx < cells.size()) {
            int curH = cells.get(idx)[0];
            int start = idx;
            while (idx < cells.size() && cells.get(idx)[0] == curH) {
                int i = cells.get(idx)[1];
                int j = cells.get(idx)[2];
                active[i][j] = true;
                cnt++;	// 새로운 영역 생성
                idx++;
            }

            for (int k = start; k < idx; k++) {
                int i = cells.get(k)[1];
                int j = cells.get(k)[2];
                int id = i * N + j;
                for (int d = 0; d < 4; d++) {
                    int ni = i + di[d];
                    int nj = j + dj[d];
                    if (ni < 0 || nj < 0 || ni >= N || nj >= N) continue;
                    if (!active[ni][nj]) continue;
                    int nid = ni * N + nj;
                    if (find(id) != find(nid)) {
                        union(id, nid);
                        cnt--;	// 두 영역 합쳐짐
                    }
                }
            }
            ans = Math.max(ans, cnt);
        }

        System.out.println(ans);
    }
}
