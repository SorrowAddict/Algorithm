import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int[][] arr;
	static boolean[][] visited;
	static ArrayDeque<int[]> q;
	static int h;

	static int[] di = {1, 0, -1, 0};
	static int[] dj = {0, 1, 0, -1};

	public static void bfs() {
		while (!q.isEmpty()) {
			int[] cur =  q.poll();
			int i = cur[0];
			int j = cur[1];

			for (int d = 0; d < 4; d++) {
				int ni = i + di[d];
				int nj = j + dj[d];
				if (0 <= ni && ni < N && 0 <= nj && nj < N) {
					if (!visited[ni][nj] && arr[ni][nj] > h) {
						visited[ni][nj] = true;
						q.offer(new int[] {ni, nj});
					}
				}
			}
		}
	}

	public static void main(String[] args) throws IOException {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			N = Integer.parseInt(br.readLine());
			arr = new int[N][N];
			int max_h = 0;
			int min_h = 100;
			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
					max_h = Math.max(max_h, arr[i][j]);
					min_h = Math.min(min_h, arr[i][j]);
				}
			}
			int ans = 0;
			for (h = min_h - 1; h <= max_h; h++) {
				visited = new boolean[N][N];
				int cnt = 0;
				for (int i = 0; i < N; i++) {
					for (int j = 0; j < N; j++) {
						if (!visited[i][j] && arr[i][j] > h) {
							visited[i][j] = true;
							q = new ArrayDeque<>();
							q.offer(new int[] {i, j});
							bfs();
							cnt++;
						}
					}
				}
				ans = Math.max(ans,  cnt);
			}
			System.out.println(ans);
	}
}
