import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			int L = Integer.parseInt(br.readLine());
			int[] S = new int[L];
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < L; i++) {
				S[i] = Integer.parseInt(st.nextToken());
			}
			int n = Integer.parseInt(br.readLine());
			Arrays.sort(S);

			int idx = Arrays.binarySearch(S, n);
			if (idx >= 0) {
				System.out.println(0);
				return;
			}

			idx = -(idx + 1);
			if (idx == 0) {
				System.out.println((n-1)*(S[0]-n-1)+(n-1)+(S[0]-n-1));
			} else {
				System.out.println((n-S[idx-1]-1)*(S[idx]-n-1)+(n-S[idx-1]-1)+(S[idx]-n-1));
			}
	}
}
