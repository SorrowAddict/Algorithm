import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			StringBuilder sb = new StringBuilder();
			int N = Integer.parseInt(br.readLine());
			String[] inputs = br.readLine().split(" ");
			int[] arr = new int[N];
			Set<Integer> set = new TreeSet<>();

			for (int i = 0; i < N; i++) {
				arr[i] = Integer.parseInt(inputs[i]);
				set.add(arr[i]);
			}
			Map<Integer, Integer> map = new HashMap<>();
			int idx = 0;
			for (int x : set) {
				map.put(x, idx++);
			}

			for (int x : arr) {
				sb.append(map.get(x) + " ");
			}
			System.out.println(sb.toString());
	}
}
