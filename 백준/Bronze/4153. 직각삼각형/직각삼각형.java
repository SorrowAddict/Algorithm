import java.io.*;
import java.util.*;

public class Main {
	public static boolean check(int[] arr) {
		Arrays.sort(arr);
		return arr[0] * arr[0] + arr[1] * arr[1] == arr[2] * arr[2];
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		while (true) {
			StringTokenizer st = new StringTokenizer(br.readLine());

			int[] arr = new int[3];
			for (int i = 0; i < 3; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}

			boolean end = false;
			for (int x : arr) {
				if (x == 0) end = true; break;
			}
			if (end) break;

			if (check(arr)) {
				System.out.println("right");
			} else {
				System.out.println("wrong");
			}
		}
	}
}
