import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
	public static void main(String[] args) throws IOException {
			BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
			int N = Integer.parseInt(br.readLine());
			int cnt = 0;

			for (int i = 0; i < N; i++) {
				Deque<Character> stack = new ArrayDeque<>();
				String input =  br.readLine();

				for (char x : input.toCharArray()) {
					if (!stack.isEmpty() && stack.getLast() == x) {
						stack.pollLast();
						continue;
					}
					stack.addLast(x);
				}
				if (stack.isEmpty()) cnt++;
			}

			System.out.println(cnt);
	}
}
