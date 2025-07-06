import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		String[] sizes = br.readLine().split(" ");
		String[] tp = br.readLine().split(" ");

		int T = Integer.parseInt(tp[0]);
		int P = Integer.parseInt(tp[1]);

		int ans_T = 0;
		for (String size : sizes) {
			int cnt = Integer.parseInt(size);
			ans_T += (cnt + T - 1) / T;
		}

		System.out.println(ans_T);
		System.out.println(N / P + " " + (N % P));
	}
}